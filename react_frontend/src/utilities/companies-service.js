import * as companiesAPI from './companies-api';


export async function fetchCompanies(filters={}) {
    return await companiesAPI.fetchCompanies();
}