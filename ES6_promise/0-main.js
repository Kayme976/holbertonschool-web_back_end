import getResponseFromAPI from "./0-main.js";

const response = getResponseFromAPI();
console.log(response instanceof Promise);
