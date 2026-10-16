from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime, timezone
from .database import Base
class PipelineMetric(Base):
    __tablename__= "pipeline_metrics"

    id = Column(Integer, primary_key=True,index=True)
    source = Column(String(100), index=True, nullable=False)
    mean_value = Column(Float, nullable=False)
    max_value = Column(Float, nullable=False)
    min_value = Column(Float, nullable=False)
    valid_count =Column(Integer, nullable=False)
    dropped_count =Column(Integer, nullable=False)
    processed_at = Column(
        DateTime(timezone=True),
        default=lambda: datetimt.now(timezone.utc),
        nullable=False,
    )
