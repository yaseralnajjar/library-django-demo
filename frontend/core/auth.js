function setCookie({ name, value, days }) {
    let date = new Date()
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000))
    document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/`
}

const getCookie = (name) => {
    const cookies = Object.assign({}, ...document.cookie.split(' ').map(cookie => {
        const name = cookie.split('=')[0]
        const value = cookie.split('=')[1]

        return { [name]: value }
    }))

    return cookies[name]
}

function deleteCookie(name) {
    document.cookie = `${name}=${getCookie(name)};expires=Thu, 01 Jan 1970 00:00:00 GMT`
}



export function persistLogin(token) {
    setCookie({ name: 'token', value: token, days: 30 })
}

export function getToken() {
    return getCookie('token')
}

export function isTokenInvalidated(responseData) {
    if (responseData.detail === 'Invalid token.') {
        deleteCookie('token')
        return true
    }

    return false
}