async function startGame() {

    const rounds =
        document.getElementById("rounds-input").value;

    const res = await fetch('/start', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rounds })
    });

    const data = await res.json();

    document.getElementById("setup-screen").style.display =
        "none";

    document.getElementById("game-screen").style.display =
        "block";

    // Enable buttons
    document.getElementById("higher-btn").disabled = false;
    document.getElementById("lower-btn").disabled = false;

    // Clear previous result
    document.getElementById("result").innerText = "";

    updateUI(data);
}


function updateUI(data) {

    document.getElementById("round").innerText =
        `Round ${data.round} / ${data.num_rounds}`;

    document.getElementById("player-number").innerText =
        data.player_number;

    document.getElementById("score").innerText =
        `Score: ${data.score}`;
}


async function sendGuess(answer) {

    const higherBtn = document.getElementById("higher-btn");
    const lowerBtn = document.getElementById("lower-btn");

    const res = await fetch('/guess', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ answer })
    });

    const data = await res.json();

    // Always update score
    document.getElementById("score").innerText =
        `Score: ${data.score}`;

    if (data.correct) {

        document.getElementById("result").innerText =
            `Correct! Computer number was ${data.computer_number}`;

    } else {

        document.getElementById("result").innerText =
            `Wrong! Computer number was ${data.computer_number}`;
    }

    if (data.game_over) {

        document.getElementById("result").innerText +=
            ` | Game Over! Final Score: ${data.score}`;

        // Disable buttons
        higherBtn.disabled = true;
        lowerBtn.disabled = true;

        return;
    }

    updateUI(data);
}