from typing import List
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str


class Post(BaseModel):
    title: str
    content: str
    author: User

class Comment(BaseModel):
    content: str
    author: User
    post:str