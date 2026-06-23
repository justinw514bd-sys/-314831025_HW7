from pydantic import BaseModel
from typing import List

class Scene(BaseModel):
    story: str

class StoryResponse(BaseModel):
    title: str
    scenes: List[Scene]