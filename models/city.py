#!/usr/bin/python3
"""Module creates User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for user objects"""

    state_id = ""
    name = ""
