from .gameparser import parse_game_result
from .queries import update_fen_node, add_move_between_nodes


def handle_game(driver, game):
    result = parse_game_result(game.headers["Result"])

    board = game.board()
    moves = game.mainline_moves()
    prev_fen = ""
    update_fen_node(driver, "", result)
    for move in list(moves):
        board.push(move)
        fen = str(board.fen())

        update_fen_node(driver, fen, result)
        add_move_between_nodes(driver, prev_fen, fen, str(move))

        prev_fen = fen