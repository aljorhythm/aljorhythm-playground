import "whatwg-fetch"

const Backend = {
    async submitSignUpForm(data) {
fetch("/api/1.0/users", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
})
    }
}

export default Backend