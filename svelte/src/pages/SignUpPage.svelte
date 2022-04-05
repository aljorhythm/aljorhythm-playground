<script>
    import Backend from "../Backend";

    let password = "",
        passwordRepeat = "",
        username, email;

    $: signUpBtnIsDisabled =     (password == "" && passwordRepeat == "") || password != passwordRepeat;

    function submitForm() {
        Backend.submitSignUpForm({
            username, email, password
        });
    }
</script>

<h1>Sign Up</h1>

<label for="username">Username</label>
<input id="username" bind:value={username} />

<label for="email">Email</label>
<input id="email" bind:value={email}/>

<label for="password">Password</label>
<input id="password" type="password" bind:value={password} />

<label for="password-repeat">Password Repeat</label>
<input id="password-repeat" type="password" bind:value={passwordRepeat} />

<button disabled={signUpBtnIsDisabled} on:click={submitForm}>Sign Up</button>
