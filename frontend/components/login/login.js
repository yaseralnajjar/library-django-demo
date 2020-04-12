import * as auth from '@core/auth.js'
import * as client from '@core/client.js'

export default function login() {
  document.getElementById('loginForm').addEventListener('submit', loginFormSubmitted)

  function loginFormSubmitted(event) {
    event.preventDefault()

    let formData = {
      username: document.getElementById('username').value,
      password: document.getElementById('password').value,
    }

    console.log(formData)

    client.login(formData).then(response => {
      console.log(response)
      auth.persistLogin(response.auth_token)
    }).catch(error => {
      console.log(error)
    })
  }
}
