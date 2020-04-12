import * as client from '@core/client.js'

export default function bookAdd() {
  document.getElementById('bookAddForm').addEventListener('submit', addBookFormSubmitted)

  function addBookFormSubmitted(event) {
    event.preventDefault()

    let formData = {
      name: document.getElementById('name').value,
      isbn: document.getElementById('isbn').value,
      publish_date: document.getElementById('publish_date').value,
    }

    console.log(formData)

    client.addBook(formData).then(response => {
      console.log(response)
    }).catch(error => {
      console.log(error)
    })
  }
}