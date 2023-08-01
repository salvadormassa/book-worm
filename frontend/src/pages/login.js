import React from "react";
import '../styles/login.css';

export default function Login() {
    return (
        <div id="login-page">
            <form id="login-form">
                <label for="userName">User Name:</label>
                <input type="text" id="userName" name="=userName" />
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" />
                <button form="login-form" type="submit">Enter</button>
            </form>
            
        </div>
    )
};