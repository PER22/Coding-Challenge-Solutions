import sendRequest from "./send-request";

const BASE_URL = '/api/solutions';

export function fetchSolutions({ language, companies, difficulty }) {
    let url = BASE_URL; // Assuming BASE_URL is something like 'http://localhost:5173/api/solutions'
    const queryParams = [];

    // Check each filter and add to queryParams array if present
    if (language) queryParams.push(`language=${encodeURIComponent(language)}`);
    if (companies && companies.length) {
        // Assuming companies is an array of strings
        companies.forEach(company => queryParams.push(`companies=${encodeURIComponent(company)}`));
    }
    if (difficulty) queryParams.push(`difficulty=${encodeURIComponent(difficulty)}`);

    // Construct the final URL with query parameters, if any
    if (queryParams.length) {
        url += `?${queryParams.join('&')}`;
    }

    // Send request to the constructed URL
    return sendRequest(url);
}