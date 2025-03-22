async function askAssistant() {
    let query = document.getElementById("query").value;
    let responseDiv = document.getElementById("response");

    if (!query.trim()) {
        responseDiv.innerHTML = "<p>Please enter a question.</p>";
        return;
    }

    responseDiv.innerHTML = "<p>Thinking...</p>";

    try {
        let response = await fetch("/query", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: query })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        let result = await response.json();
        responseDiv.innerHTML = `<p>${result.response || "No response received"}</p>`;
    } catch (error) {
        console.error("Error:", error);
        responseDiv.innerHTML = `<p>Error: ${error.message}</p>`;
    }
}
