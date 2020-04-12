import bookAdd from '@components/book-add/book-add.js'
import booksList from '@components/books-list/books-list.js'
import login from '@components/login/login.js'
import register from '@components/register/register.js'
import { Router } from '@core/router.js'

const routes = {
  '/login.html': login,
  '/register.html': register,
  '/register.html': register,
  '/book-add.html': bookAdd,
  '/books-list.html': booksList,
}
const router = new Router(routes)
router.init()