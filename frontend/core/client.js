function url(appendedURL) {
  let baseURL = 'http://127.0.0.1:8000/api'
  return baseURL + appendedURL
}

export async function registerNewUser(data) {
  const response = await fetch(url('/auth/users/'), {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  })

  return await response.json()
}

export async function login(data) {
  const response = fetch(url('/auth/users/login/'), {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  })

  return await response.json()
}
