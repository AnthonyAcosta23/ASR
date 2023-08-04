  // Assuming you have a server-side API for handling call status
  
  document.addEventListener("DOMContentLoaded", function () {
    const incomingCallElement = document.getElementById("incoming-call");
    const answerBtn = document.getElementById("answer-btn");
    const hangupBtn = document.getElementById("hangup-btn");
  
    // Function to fetch call status from the server
    function fetchCallStatus() {
      // Replace 'your-api-url' with your server API endpoint to get call status
      fetch("your-api-url")
        .then((response) => response.json())
        .then((data) => {
          // Assuming the response contains the call status, e.g., { status: 'incoming' }
          const callStatus = data.status;
          if (callStatus === "incoming") {
            incomingCallElement.innerText = "Incoming Call";
            answerBtn.disabled = false;
          } else {
            incomingCallElement.innerText = "No incoming call";
            answerBtn.disabled = true;
          }
        })
        .catch((error) => {
          console.error("Error fetching call status:", error);
        });
    }
  
    // Function to handle answering the call
    function answerCall() {
      // Implement the logic to answer the call using your server API
      // For example: fetch("your-api-url/answer", { method: "POST" });
      console.log("Answering the call...");
    }
  
    // Function to handle hanging up the call
    function hangupCall() {
      // Implement the logic to hang up the call using your server API
      // For example: fetch("your-api-url/hangup", { method: "POST" });
      console.log("Hanging up the call...");
    }

    // Funtion to handle closing up the call
    function closeupcall() {
      // Implement the logs to close up the calls using your server API
      // For example: fetch("your-api-url/closeup", {method: "POST"});
      console.log("Close up the calls");
    }

    // Funtion to handle notes panel
    function notespane() {
      // Implements the logs to close up the calls using your server API
      // for example: fetch("your-api-url/notes panel", {methods: "POST"});
      console.log("Notes Panel");
    }

    // Funtion for quality Assurance (QA) Survey
    function QA() {
      // Implemets the qa logs to qualify the calls and score using your API
      // For example: fetch("your-api-url/notes panel", {methods: "POST"});
      console.log("QA score")
    }
  
    // Fetch initial call status on page load
    fetchCallStatus();
  
    // Add event listeners to buttons
    answerBtn.addEventListener("click", answerCall);
    hangupBtn.addEventListener("click", hangupCall);
  });