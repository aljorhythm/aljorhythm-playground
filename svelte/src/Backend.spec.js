import Backend from "./Backend"
import "whatwg-fetch"

test("submit sign up form", () => {
    let mockFn = jest.fn()
    window.fetch = mockFn
    let data = {}
    Backend.submitSignUpForm(data)
    let path = '/api/1.0/users'
    let options = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    }
 
    const firstCall = mockFn.mock.calls[0]
    const [gotPath, gotOptions] = [firstCall[0], firstCall[1]]
    expect(gotOptions).toEqual(options)
    expect(gotPath).toEqual(path)
})