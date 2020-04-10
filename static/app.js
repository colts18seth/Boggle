let score = 0;
let time = 60;
$('#score').text(score);
$('#time').text(time);

$(".guess").prepend("<p class='result'></p>");

$("#startButton").on("click", function () {
    $("#startButton").hide();
    $("#table").show();
    $("#guessForm").show();
    let guessForm = $("#guessForm");
    countdown(time, guessForm)
});

$("#guessForm").on("submit", async function (e) {
    e.preventDefault();
    let newGuess = $("#guessText").val();
    if (newGuess === "") {
        return
    }
    let guessLength = newGuess.length;

    let res = await axios.post("/guess", {
        guess: newGuess
    });
    $("#guessText").val("");

    if (res.data == "ok") {
        score += guessLength;
        $("#score").text(score);
        $(".result").text("Word added! Keep Going")
    } else if (res.data == "not-word") {
        $(".result").text("Not a Word! Try another")
    } else if (res.data == "not-on-board") {
        $(".result").text("Word Not on Board! Try Another")
    } else {
        $(".result").text("Error!")
    };
});

function countdown(time, hideThis) {
    interval = setInterval(function () {
        time--;
        $("#time").text(time);
        if (!time) {
            clearInterval(interval);
            hideThis.hide()
            saveScoreAndTimesPlayed()
        }
    }, 1000)
}

function saveScoreAndTimesPlayed() {
    let score = $("#score").text();
    let res = await axios.post("/save", {
        score: score
    });
}