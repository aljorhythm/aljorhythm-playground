import SignUpPage from './SignUpPage.svelte';
import { render, screen } from '@testing-library/svelte';
import userEvent from '@testing-library/user-event'
import '@testing-library/jest-dom';

describe("Sign Up Page", () => {
    describe("Layout", () => {
        test('it has sign up header', () => {
            render(SignUpPage);
            const header = screen.getByRole('heading', { name: 'Sign Up' });
            expect(header).toBeInTheDocument()
        })
        test('has username input', () => {
            render(SignUpPage);
            const input = screen.getByLabelText("Username")
            expect(input).toBeInTheDocument()
        })
        test('has e-mail input', () => {
            render(SignUpPage);
            const input = screen.getByLabelText("Email")
            expect(input).toBeInTheDocument()
        })
        test('has password input', () => {
            render(SignUpPage);
            const input = screen.getByLabelText("Password")
            expect(input).toBeInTheDocument()
            expect(input.type).toBe("password")
        })
        test('has password repeat input', () => {
            render(SignUpPage);
            const input = screen.getByLabelText("Password Repeat")
            expect(input).toBeInTheDocument()
            expect(input.type).toBe("password")
        })
        it("has Sign Up button", () => {
            render(SignUpPage)
            const button = screen.getByRole("button", {
                name: "Sign Up"
            })
            expect(button).toBeDisabled()
        })
    })

    describe("Interactions", () => {
        it("enables the sign up button when password and password repeat fields are equal", async () => {
            render(SignUpPage)
            const passwordInput = screen.getByLabelText("Password")
            const passwordRepeatInput = screen.getByLabelText("Password Repeat")
            const passwordValue = "abc123"
            await userEvent.type(passwordInput, passwordValue)
            await userEvent.type(passwordRepeatInput, passwordValue)
            const button = screen.getByRole("button", { name: "Sign Up" })
            expect(button).toBeEnabled()
        })
    })
})