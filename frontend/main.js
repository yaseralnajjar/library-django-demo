import login from '@components/login/login.js'
import register from '@components/register/register.js'
import { Router } from '@core/router.js'

const routes = {
  '/login.html': login,
  '/register.html': register,
}
const router = new Router(routes)
router.init()