import React from "react";
import '../styles/booksearch.css';

export default function BookSearch () {
    return (
        <div id="book-search-page">
            <form id="book-search-form">
                <div>
                <label>
                    ISBN:
                    <input type="text" name="isbn" />
                </label>
                </div>
                <div>
                <label>
                    Title:
                    <input type="text" name="title" />
                </label>
                </div>
                <div>
                <button form="book-search-form" type="submit" />
                </div>
            </form>
        </div>
    )
};