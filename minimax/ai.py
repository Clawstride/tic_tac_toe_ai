EMPTY = ""
WINNING_PATTERNS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def get_winner(board):
    validate_board(board)

    for first, second, third in WINNING_PATTERNS:
        if board[first] != EMPTY and board[first] == board[second] == board[third]:
            return board[first]

    return None


def is_draw(board):
    validate_board(board)
    return get_winner(board) is None and all(cell != EMPTY for cell in board)


def available_moves(board):
    validate_board(board)
    return [index for index, cell in enumerate(board) if cell == EMPTY]


def evaluate_board(board, ai_player="O", human_player="X"):
    winner = get_winner(board)

    if winner == ai_player:
        return 10

    if winner == human_player:
        return -10

    return 0


def best_move(board, ai_player="O", human_player="X"):
    validate_players(ai_player, human_player)
    validate_board(board)

    if get_winner(board) is not None or is_draw(board):
        return None

    best_score = float("-inf")
    move = None

    for index in available_moves(board):
        next_board = board.copy()
        next_board[index] = ai_player
        score = minimax(next_board, False, ai_player, human_player, 0)

        if score > best_score:
            best_score = score
            move = index

    return move


def minimax(board, is_maximizing, ai_player="O", human_player="X", depth=0):
    score = evaluate_board(board, ai_player, human_player)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")

        for index in available_moves(board):
            next_board = board.copy()
            next_board[index] = ai_player
            best_score = max(
                best_score,
                minimax(next_board, False, ai_player, human_player, depth + 1),
            )

        return best_score

    best_score = float("inf")

    for index in available_moves(board):
        next_board = board.copy()
        next_board[index] = human_player
        best_score = min(
            best_score,
            minimax(next_board, True, ai_player, human_player, depth + 1),
        )

    return best_score


def validate_board(board):
    if len(board) != 9:
        raise ValueError("Board must contain exactly 9 cells.")

    invalid_cells = [cell for cell in board if cell not in ("X", "O", EMPTY)]

    if invalid_cells:
        raise ValueError("Board cells must be 'X', 'O', or an empty string.")


def validate_players(ai_player, human_player):
    if ai_player == human_player:
        raise ValueError("AI player and human player must be different.")

    if ai_player not in ("X", "O") or human_player not in ("X", "O"):
        raise ValueError("Players must be 'X' or 'O'.")


def run_self_tests():
    assert evaluate_board(["O", "O", "O", "", "", "", "", "", ""]) == 10
    assert evaluate_board(["X", "X", "X", "", "", "", "", "", ""]) == -10
    assert is_draw(["X", "O", "X", "X", "O", "O", "O", "X", "X"])

    winning_board = ["O", "O", "", "X", "X", "", "", "", ""]
    assert best_move(winning_board) == 2

    blocking_board = ["X", "X", "", "O", "", "", "", "", ""]
    assert best_move(blocking_board) == 2

    fork_risk_board = ["X", "", "", "", "O", "", "", "", "X"]
    assert best_move(fork_risk_board) in (1, 3, 5, 7)

    forced_draw_board = ["X", "O", "X", "X", "O", "", "O", "X", ""]
    assert best_move(forced_draw_board) == 5


if __name__ == "__main__":
    run_self_tests()
    print("Minimax AI self-tests passed.")
