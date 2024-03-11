import sendRequest from "./send-request";

const BASE_URL = '/api/companies';

export function fetchCompanies() {
    return sendRequest(BASE_URL);
}