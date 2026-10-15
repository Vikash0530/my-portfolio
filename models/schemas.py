from pydantic import BaseModel, EmailStr, Field
from typing import List


class ContactRequest(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr

    message: str = Field(
        min_length=10,
        max_length=2000
    )


class Project(BaseModel):

    title: str
    description: str
    tech_stack: List[str]
    metric: str
    github_url: str