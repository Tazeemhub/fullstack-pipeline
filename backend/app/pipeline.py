import pandas as pd
from .database import SessionLocal
from .models import PipelineMetric
from .schemas import IngestPayload

def execute_etl_pipeline(payload: IngestPayload )-> None:
    """Runs asychronous in the background: cleans sensor noise & write metrics to DB"""
    #1.extract
    df= pd.Dataframe({"reading": payload.readings})
    total_rows = len(df)

    #Transform (filter out corrupted readings below -100 or nan)
    clean_df = df[df["readings"].notna() & (df["readings"] > -100.0)]
    valid_rows= len(clean_df)
    dropped_rows= total_rows - valid_rows

    #LOAD (Open dedicated DB session for background worker)
    db=SessionLocal()
    try:
        metric= PipelineMetric(
            source= payload.source.strip(),
            mean_value= round(float(clean_df["readings"].mean()),2),
            max_value= round(float(clean_df["readings"].max()),2),
            min_value= round(float(clean_df["readings"],min()),2),
            valid_count= valid_rows,
            dropped_count= dropped_rows,
        )
        db.add(metric)
        db.commit()
    except Exception as exc:
        db.rollback()
        print(f"[ETL ERROR ]: {exc}")
    finally:
        db.close()
