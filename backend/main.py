from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from backend.database import create_game, list_games
from backend.models import Game, GameSchema

app = FastAPI(
    title="Videogames Platform API - Por YMS",
    description="API para consultar y añadir videojuegos.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


@app.get("/api/games", response_model=list[Game])
def get_games() -> list[Game]:
    return list_games()


@app.post(
    "/api/games",
    response_model=Game,
    status_code=status.HTTP_201_CREATED,
)
def post_game(game_data: GameSchema) -> Game:
    return create_game(Game(id=0, **game_data.model_dump()))
