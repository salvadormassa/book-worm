import React from "react";

export default function Login() {
    return (
        <div>
            <form id="login-form">
                <label for="userName">User Name:</label>
                <input type="text" id="userName" name="=userName" />
                <label for="password">Password:</label>
                <input type="text" id="password" name="password" />
            </form>
        </div>
    )
};