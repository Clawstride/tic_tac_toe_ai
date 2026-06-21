const cells = document.querySelectorAll(".cell");
const boardElement = document.querySelector(".board");
const resetButton = document.querySelector("#reset-button");
const statusArea = document.querySelector("#game-status");
const aiMoveUrl = boardElement.dataset.aiUrl;

const winningPatterns = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
];

let board = ["", "", "", "", "", "", "", "", ""];
let gameActive = true;
let waitingForAi = false;

cells.forEach((cell) => {
    cell.addEventListener("click", async () => {
        const cellIndex = Number(cell.dataset.cell);

        if (!gameActive || waitingForAi || board[cellIndex] !== "") {
            return;
        }

        placeMove(cell, cellIndex, "X");

        if (finishGameIfNeeded()) {
            return;
        }

        waitingForAi = true;
        statusArea.textContent = "AI is thinking...";

        try {
            const aiMove = await requestAiMove();

            if (aiMove !== null && board[aiMove] === "") {
                placeMove(cells[aiMove], aiMove, "O");
            }

            if (!finishGameIfNeeded()) {
                statusArea.textContent = "Your turn.";
            }
        } catch (error) {
            statusArea.textContent = "AI move failed. Please try again.";
        } finally {
            waitingForAi = false;
        }
    });
});

resetButton.addEventListener("click", () => {
    board = ["", "", "", "", "", "", "", "", ""];
    gameActive = true;
    waitingForAi = false;
    statusArea.textContent = "Your turn.";

    cells.forEach((cell) => {
        cell.textContent = "";
        cell.disabled = false;
        cell.classList.remove("cell-selected", "cell-ai", "cell-win");
        cell.setAttribute("aria-label", `Cell ${Number(cell.dataset.cell) + 1}`);
    });
});

function placeMove(cell, cellIndex, player) {
    board[cellIndex] = player;
    cell.textContent = player;
    cell.disabled = true;
    cell.classList.add("cell-selected");

    if (player === "O") {
        cell.classList.add("cell-ai");
    }

    cell.setAttribute("aria-label", `Cell ${cellIndex + 1}, Player ${player}`);
}

function getWinningPattern() {
    for (const pattern of winningPatterns) {
        const [first, second, third] = pattern;

        if (
            board[first] !== "" &&
            board[first] === board[second] &&
            board[first] === board[third]
        ) {
            return pattern;
        }
    }

    return null;
}

function finishGameIfNeeded() {
    const winningPattern = getWinningPattern();

    if (winningPattern) {
        gameActive = false;
        highlightWinningCells(winningPattern);
        statusArea.textContent = board[winningPattern[0]] === "X" ? "You win!" : "AI wins!";
        disableBoard();
        return true;
    }

    if (isDraw()) {
        gameActive = false;
        statusArea.textContent = "It's a draw!";
        disableBoard();
        return true;
    }

    return false;
}

function isDraw() {
    return board.every((cell) => cell !== "");
}

function disableBoard() {
    cells.forEach((cell) => {
        cell.disabled = true;
    });
}

function highlightWinningCells(pattern) {
    pattern.forEach((index) => {
        cells[index].classList.add("cell-win");
    });
}

async function requestAiMove() {
    const response = await fetch(aiMoveUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ board }),
    });

    if (!response.ok) {
        throw new Error("AI request failed.");
    }

    const data = await response.json();
    return data.move;
}
