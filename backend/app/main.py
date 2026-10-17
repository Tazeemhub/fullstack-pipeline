from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class IngestPayload(BaseModel):
    source: str = Field(..., min_length=2, max_length=100, example=["telemetry_node_01"])
    readings: list[float] = Field(..., min_length=1, examples=[[24.5,26.1, -999.0,25.0]])

class MetricResponse(BaseModel):
    id: int
    source: str
    mean_value: float
    max_value: float
    min_value: float
    valid_count: int
    dropped_count: int
    processed_at: datetime

    model_config= ConfigDict(from_attributes=True)