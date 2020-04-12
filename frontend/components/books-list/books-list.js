import * as client from '@core/client.js'
import { htmlElement } from '@core/html-element.js'

export default function booksList() {

  client.getBooks().then(response => {
    console.log(response)
    renderBooks(response)
  }).catch(error => {
    console.log(error)
  })

  function createBookSection(book) {
    const p = htmlElement.create('section')
      .addChildren(
        [
          {
            elem: 'div',
            children:
              [
                {
                  elem: 'div',
                  text: 'Name:'
                },
                {
                  elem: 'div',
                  text: book.name
                },
              ]
          },


          {
            elem: 'div',
            children: [
              {
                elem: 'div',
                inner: 'ISBN:'
              },
              {
                elem: 'div',
                text: book.isbn
              },
            ]
          },

          {
            elem: 'div',
            children: [
              {
                elem: 'div',
                text: 'Publish Date:'
              },
              {
                elem: 'div',
                text: book.publish_date
              },
            ]
          },
        ])
      .element
    return p
  }

  function renderBooks(books) {
    const articleElement = document.getElementsByTagName('article')[0]

    books.forEach(book => {
      articleElement.appendChild(createBookSection(book))
    })
  }
}