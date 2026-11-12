from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.database import create_game, list_games, set_game_rating
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


@app.post("/api/games/{game_id}/rate")
def rate_game(game_id: int, rating: int):
    if rating < 1 or rating > 5:
        raise HTTPException(status_code=400, detail="La calificacion debe ser entre 1 y 5")
    if set_game_rating(game_id, rating) is None:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
    return {"game_id": game_id, "rating": rating, "status": "calificacion registrada"}


# --- Módulo de Reseñas (Feature B) ---
@app.post("/api/games/{game_id}/review")
def review_game(game_id: int, comment: str):
    if not comment or len(comment.strip()) == 0:
        game = next((g for g in list_games() if g.id == game_id), None)
      
        raise HTTPException(status_code=400, detail="El comentario no puede estar vacio")
    
    if not game:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
    return {"game_id": game_id, "comment": comment.strip(), "status": "resena publicada"}
