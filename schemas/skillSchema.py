from pydantic import BaseModel, Field


class skillSchema(BaseModel):
    skillName: str = Field(min_length=3, max_length=20)
