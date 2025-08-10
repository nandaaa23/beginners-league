const output = document.getElementById("output");
    const button = document.getElementById("generate");

    button.addEventListener("click", async () => {
      output.textContent = "Generating joke... 🤔";

      try {
        const response = await fetch("/generate-joke", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ prompt: "Tell me a silly, light-hearted joke in 1-2 sentences." }),
        });

        if (!response.ok) {
          const error = await response.json();
          output.textContent = `Error: ${error.error || "Unknown error"}`;
          return;
        }

        const data = await response.json();
        const joke = data.choices?.[0]?.message?.content || "No joke returned.";
        output.textContent = joke;
      } catch (err) {
        output.textContent = "Error: " + err.message;
      }
    });