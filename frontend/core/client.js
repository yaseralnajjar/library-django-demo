import * as auth from '@core/auth.js'


function url(appendedURL) {
  let baseURL = 'http://127.0.0.1:8000/api'
  return baseURL + appendedURL
}

function rerouteToLogin() {
  window.location.assign('/login.html')
}


async function request(path, data, withCredentials = false) {
  const options = {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  }

  if (withCredentials) {
    const token = auth.getToken()
    options.headers.Authorization = `Token ${token}`
  }

  const response = await fetch(url(path), options)

  const result = await response.json()

  if (auth.isTokenInvalidated(result)) {
    rerouteToLogin()
  }

  return result
}

export async function registerNewUser(data) {
  return request('/auth/users/', data)
}

export async function login(data) {
  return request('/auth/users/login/', data)
}

export async function getBooks() {
  const response = await fetch(url('/books/'), {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    }
  })

  return await response.json()
}

export async function addBook(data) {
  const withCredentials = true
  return await request('/books/', data, withCredentials)
}

