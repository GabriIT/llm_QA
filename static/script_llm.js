const form = document.getElementById('queryForm');
const queryInput = document.getElementById('queryInput');
const responseContainer = document.getElementById('responseContainer');

form.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent form from refreshing the page

    const Question = queryInput.value; 

    // Make AJAX request to your Flask app
    fetch('/query', { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ Question : Question }) 
    })
    .then(response => response.json()) // Parse the response as JSON
    .then(data => {
        // Display the response in the modal
        responseContainer.textContent = data.response;
        $('#responseModal').modal('show'); // Show the modal using Bootstrap
    })
    .catch(error => {
        console.error('Error:', error);
    });
});