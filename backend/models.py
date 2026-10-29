from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class CategoryEnum(str, Enum):
    ACTION = "Acción"
    ADVENTURE = "Aventura"
    STRATEGY = "Estrategia"
    SPORTS = "Deportes"
    RPG = "RPG"
    OTHER = "Otro"


class GameSchema(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=1, max_length=100)
    genre: CategoryEnum
    platform: str = Field(min_length=1, max_length=50)
    release_year: int = Field(ge=1950, le=2100)
    description: str = Field(default="", max_length=500)


class Game(GameSchema):
    id: int
