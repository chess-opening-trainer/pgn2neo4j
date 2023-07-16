from .gameparser import read_games
from .gamehandler import handle_game

def pgn2neo4j(path, driver, show_progress=False):
    with driver.session() as session:
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (p:Position) REQUIRE p.fen IS UNIQUE")

    games = list(read_games(path))

    if show_progress:
        from tqdm import tqdm
        games = tqdm(games)

    for game in games:
        handle_game(driver, game)