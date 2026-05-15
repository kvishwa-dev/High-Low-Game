from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

MAX_ROUNDS = 15

game_data = {
    "score": 0,
    "round": 1,
    "num_rounds": 5,
    "player_number": 0,
    "computer_number": 0
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start_game():

    data = request.json
    rounds = int(data["rounds"])

    if rounds < 1 or rounds > MAX_ROUNDS:
        return jsonify({
            "error": "Rounds must be between 1 and 15"
        }), 400

    game_data["score"] = 0
    game_data["round"] = 1
    game_data["num_rounds"] = rounds

    game_data["player_number"] = random.randint(1, 100)
    game_data["computer_number"] = random.randint(1, 100)

    return jsonify({
        "round": game_data["round"],
        "num_rounds": game_data["num_rounds"],
        "player_number": game_data["player_number"],
        "score": game_data["score"]
    })


@app.route("/guess", methods=["POST"])
def guess():

    data = request.json
    ans = data["answer"]

    a = game_data["player_number"]
    b = game_data["computer_number"]

    correct = False

    if ans == "higher" and a > b:
        correct = True

    elif ans == "lower" and a < b:
        correct = True

    if correct:
        game_data["score"] += 1

    response = {
        "correct": correct,
        "computer_number": b,
        "score": game_data["score"],
        "num_rounds": game_data["num_rounds"]
    }

    game_data["round"] += 1

    if game_data["round"] > game_data["num_rounds"]:
        response["game_over"] = True
        return jsonify(response)

    game_data["player_number"] = random.randint(1, 100)
    game_data["computer_number"] = random.randint(1, 100)

    response["round"] = game_data["round"]
    response["player_number"] = game_data["player_number"]

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)