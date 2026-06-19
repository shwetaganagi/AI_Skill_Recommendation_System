from pydantic import BaseModel, Field


class UserInput(BaseModel):
    skills: str
    education: str
    interests: str
    experience: int = Field(ge=0, le=30)