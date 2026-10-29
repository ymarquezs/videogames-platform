const API_URL = "http://127.0.0.1:8000/api/games";

const gameList = document.querySelector("#game-list");
const gameCount = document.querySelector("#game-count");
const notice = document.querySelector("#notice");
const gameForm = document.querySelector("#game-form");
const submitButton = gameForm.querySelector('button[type="submit"]');

function showNotice(message, isError = false) {
  notice.textContent = message;
  notice.classList.toggle("error", isError);
}

function createGameCard(game) {
  const card = document.createElement("article");
  card.className = "game-card";

  const meta = document.createElement("div");
  meta.className = "game-meta";

  const genre = document.createElement("span");
  genre.className = "game-tag genre-tag";
  genre.textContent = game.genre;

  const platform = document.createElement("span");
  platform.className = "game-tag";
  platform.textContent = game.platform;

  const year = document.createElement("span");
  year.className = "game-tag";
  year.textContent = String(game.release_year);

  const title = document.createElement("h3");
  title.textContent = game.title;

  const description = document.createElement("p");
  description.textContent = game.description || "Sin descripción.";

  meta.append(genre, platform, year);
  card.append(meta, title, description);
  return card;
}

function renderGames(games) {
  gameList.replaceChildren();
  gameCount.textContent = `${games.length} ${games.length === 1 ? "juego" : "juegos"}`;

  if (games.length === 0) {
    const emptyState = document.createElement("p");
    emptyState.className = "empty-state";
    emptyState.textContent = "Todavía no hay juegos. ¡Añade el primero a tu colección!";
    gameList.append(emptyState);
    return;
  }

  gameList.append(...games.map(createGameCard));
}

async function loadGames({ clearNotice = true } = {}) {
  if (clearNotice) {
    showNotice("");
  }
  gameCount.textContent = "Cargando juegos…";

  try {
    const response = await fetch(API_URL);
    if (!response.ok) {
      throw new Error(`El servidor respondió con el estado ${response.status}.`);
    }

    renderGames(await response.json());
  } catch (error) {
    gameCount.textContent = "No disponible";
    showNotice(
      `No se pudo cargar el catálogo. Comprueba que la API esté activa en http://127.0.0.1:8000. ${error.message}`,
      true,
    );
  }
}

gameForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  showNotice("");
  submitButton.disabled = true;

  const formData = new FormData(gameForm);
  const game = Object.fromEntries(formData.entries());
  game.release_year = Number(game.release_year);

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(game),
    });

    if (!response.ok) {
      const errorBody = await response.json();
      const details = Array.isArray(errorBody.detail)
        ? errorBody.detail.map((item) => item.msg).join(", ")
        : errorBody.detail;
      throw new Error(details || `El servidor respondió con el estado ${response.status}.`);
    }

    gameForm.reset();
    showNotice("Videojuego añadido correctamente.");
    await loadGames({ clearNotice: false });
  } catch (error) {
    showNotice(`No se pudo añadir el videojuego. ${error.message}`, true);
  } finally {
    submitButton.disabled = false;
  }
});

loadGames();
