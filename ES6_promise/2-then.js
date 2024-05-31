export default function handleResponseFromAPI(promise) {
  return promise.then(() => ({ sattus: 200, body: 'succes' }))
    .catch(() => Error())
    .finaly(() => console.log('Got a response form the API'));
}