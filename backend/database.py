from backend.models import CategoryEnum, Game


_games: list[Game] = [
    Game(
        id=1,
        title="The Legend of Zelda: Breath of the Wild",
        genre=CategoryEnum.ADVENTURE,
        platform="Nintendo Switch",
        release_year=2017,
        description="Una aventura de mundo abierto en el reino de Hyrule.",
    ),
    Game(
        id=2,
        title="Hades",
        genre=CategoryEnum.ACTION,
        platform="PC",
        release_year=2020,
        description="Lucha para escapar del inframundo en este roguelike de acción.",
    ),
]
_next_id = 3


def list_games() -> list[Game]:
    return list(_games)


def create_game(game_data: Game) -> Game:
    global _next_id
    game = game_data.model_copy(update={"id": _next_id})
    _next_id += 1
    _games.append(game)
    return game
