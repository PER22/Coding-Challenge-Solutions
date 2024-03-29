// import { getToken } from "./users-service";
export default async function sendRequest(url, method = 'GET', payload=null, headers = {}){
    const options = { method, headers };
    // if(payload){
    //     if (payload instanceof FormData) {
    //         options.body = payload;
    //     } else {
    //         options.headers['Content-Type'] = 'application/json';
    //         options.body = JSON.stringify(payload);
    //     }
    // }
    
    // const token = getToken();
    // if(token){
    //     options.headers.Authorization = `Bearer ${token}`;
    // }
    const res = await fetch(url, options);
    
    if (res.ok){
        const contentType = res.headers.get("content-type");
        if (contentType && contentType.includes("application/json")) {
            return res.json();
        } else {
            return res.text();
        }
    } else {
        const errorData = await res.json(); // Assume server always sends JSON error responses
        return {error: errorData.error};
    }
}