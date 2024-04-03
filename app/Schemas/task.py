from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TaskBaseSchema(BaseModel):
    # id: Optional[int] = None
    user_id: int = Field(default=1)
    title: Optional[str] = None
    description: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "Sample Task",
                "description": "This is a sample task description."
            }
        }
