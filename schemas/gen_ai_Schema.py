from pydantic import BaseModel, Field


class gen_ai_Schema(BaseModel):
    message: str = Field(min_length=0, max_length=2000)
