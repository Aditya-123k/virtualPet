async function runMain() {
    try {
        const response = await fetch('/run-main', {
            method: 'POST',  // Send POST request to Flask
        });

        const data = await response.json();  // Parse JSON response
        
        if (response.ok) {
            console.log("Script output:", data.output);  // Log script output
            alert("Script executed successfully!");  // Alert the user
        } else {
            console.error("Error:", data.error);  // Log any error
            alert("Error executing script.");  // Alert the user
        }
    } catch (error) {
        console.error("Request failed:", error);  // Log request failure
        alert("An error occurred.");  // Alert the user
    }
}
