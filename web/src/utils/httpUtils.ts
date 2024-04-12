type RequestParams = {
  url: string
  requestParams?: {[key: string]: any}
}

const getDefaultHttpParams = () => {
  // const apiKey = getDataFromLocalStorage("apiKey") || await generateAPIKey();

  const headers = new Headers({
    'Content-Type': 'application/json'
  })

  return { headers };
}

const buildUrlEncodedParams = (params: { [key: string]: string | number | boolean }) => Object.keys(params).map((key) => `${key}=${encodeURIComponent(params[key])}`).join('&');

const get = async (params: RequestParams) => {
  const urlQueryString = params.requestParams ? `?${buildUrlEncodedParams(params.requestParams)}` : '';
  const requestURL = `${params.url}${urlQueryString}`;

  const response = await fetch(requestURL, getDefaultHttpParams());

  if (!response.ok) {
    throw new Error(JSON.stringify({
      error: "Something went wrong while processing this request", 
      message: response.body,
      status: response.status
    }))
  }

  return response.json()
}

const post = async (params: RequestParams) => {
  const response = await fetch(params.url, Object.assign(
    {}, 
    getDefaultHttpParams(), 
    {
      method: 'POST',
      body: JSON.stringify(params.requestParams),
    }
  ));

  if (!response.ok) {
    throw new Error(JSON.stringify({
      error: response.body, 
      status: response.status
    }))
  }
  return response.json()
}

export default { get, post }