from flask import Flask, jsonify, render_template, request

from minimax.ai import best_move, get_winner, is_draw


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ai-move", methods=["POST"])
def ai_move():
    data = request.get_json(silent=True) or {}
    board = data.get("board")

    if not isinstance(board, list):
        return jsonify({"error": "Board must be provided as a list."}), 400

    try:
        winner = get_winner(board)
        draw = is_draw(board)
        move = None if winner or draw else best_move(board)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    return jsonify({
        "move": move,
        "winner": winner,
        "draw": draw,
    })


if __name__ == "__main__":
    app.run(debug=True)
