import * as solutionsAPI from './solutions-api';


export async function fetchSolutions(filters={}) {
    const response = await solutionsAPI.fetchSolutions({
        language: filters.language || null, 
        companies: filters.companies || null, 
        difficulty: filters.difficulty || null});
        console.log("Response: ", response);
    return response;
}