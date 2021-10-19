from typing import List, Optional
from pydantic import BaseModel

# Creates a blue print for the blog schema with it's default attributes 
class BlogBase(BaseModel):
    title: str
    description: Optional[str] = None
    content: str 

# Creates attribute upon creation of any blog, with default attributes inherited from the BlogBase schema
class BlogCreate(BlogBase):
    pass 

# Creates the main blog with other attributes plus the ones inherited from the BlogBase schema
class Blog(BlogBase):
    id: int 
    owner_id: int 

    class Config:
        orm_mode: True

# Creates a user base schema with a default attribute here email
class UserBase(BaseModel):
    email: str 

# This will require the password attribute of a user when creating a new user
class UserCreate(UserBase):
    password: str 

# The main user class with it's other attribute 
class User(UserBase):
    id: int 
    is_active: bool
    blogs: List[Blog] = []

    class Config:
        orm_mode: True