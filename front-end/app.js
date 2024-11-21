async function downloadVideo() {
   const url = document.getElementById('url').value;
   const messageDiv = document.getElementById('message');

   if (!url) {
       messageDiv.innerText = 'Please enter a URL!';
       messageDiv.style.color = 'red';
       return;
   }

   messageDiv.innerText = 'Downloading...';
   messageDiv.style.color = 'blue';

   try {
       const response = await fetch('http://127.0.0.1:5000/download', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json'
           },
           body: JSON.stringify({ url: url })
       });

       const data = await response.json();

       if (response.ok) {
           messageDiv.innerText = `Video: ${data.video_title} is downloading...`;
           messageDiv.style.color = 'green';
       } else {
           messageDiv.innerText = `Error: ${data.error}`;
           messageDiv.style.color = 'red';
       }
   } catch (error) {
       messageDiv.innerText = 'An error occurred.';
       messageDiv.style.color = 'red';
   }
}