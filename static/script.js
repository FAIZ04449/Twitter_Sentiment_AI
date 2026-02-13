async function analyze() {
    const text = document.getElementById("tweetInput").value;

    const response = await fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });

    const data = await response.json();

    let sentimentClass = "";

    if (data.sentiment === "Positive") {
        sentimentClass = "positive";
    } else if (data.sentiment === "Negative") {
        sentimentClass = "negative";
    } else {
        sentimentClass = "neutral";
    }

    document.getElementById("result").innerHTML =
        `<div class="result-card">
            <p><strong>Original:</strong> ${data.original_text}</p>
            <p><strong>Cleaned:</strong> ${data.cleaned_text}</p>
            <p>Sentiment: <span class="${sentimentClass}">${data.sentiment}</span></p>
            <p>Compound Score: ${data.compound_score}</p>
        </div>`;
}
