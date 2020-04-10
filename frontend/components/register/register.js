import * as client from '@core/client.js'

export default function register() {
  document.getElementById('registerForm').addEventListener('submit', registerFormSubmitted)

  function registerFormSubmitted(event) {
    event.preventDefault()

    let formData = {
      first_name: document.getElementById('firstname').value,
      username: document.getElementById('username').value,
      password: document.getElementById('password').value,
    }

    console.log(formData)

    client.registerNewUser(formData).then(response => {
      console.log(response)
    }).catch(error => {
      console.log(error)
    })
  }
}