// // Function to fetch quotes from the Quotes API
// function fetchQuotes() {
//   const apiKey = 'WFJ8QYLApcgZcx6aBHI77w==WHpaJ2lrcTfwAN6I'; // Replace with your actual API key
//   const category = 'happiness'; // You can change the category as desired

//   return fetch(`https://api.api-ninjas.com/v1/quotes?category=${category}`, {
//       headers: {
//           'X-Api-Key': apiKey,
//           'Content-Type': 'application/json'
//       }
//   })
//       .then(response => response.json())
//       .then(data => data)
//       .catch(error => {
//           console.error('Error fetching quotes:', error);
//           return [];
//       });
// }

// // Function to get a random quote
// async function getRandomQuote() {
//   const quotes = await fetchQuotes();
//   return quotes[Math.floor(Math.random() * quotes.length)];
// }

// // Function to handle the redirect
// async function redirectWithQuote() {
//   // Get the current URL
//   const currentUrl = window.location.href;

//   // Check if the URL already has the 'to' query parameter
//   const urlParams = new URLSearchParams(window.location.search);
//   const hasQuoteParam = urlParams.has('to');

//   if (!hasQuoteParam) {
//       // Fetch a random quote
//       const quote = await getRandomQuote();

//       // Construct the new URL with the quote
//       const newUrl = `${currentUrl}?to=${encodeURIComponent(quote.quote)}`;

//       // Redirect to the new URL
//       window.location.href = newUrl;
//   }
// }

// // Call the redirect function when the page loads
// window.addEventListener('load', redirectWithQuote);