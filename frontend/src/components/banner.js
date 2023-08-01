import React from "react";
import  '../styles/banner.css';

export default function Banner({ currentPage, handlePageChange }) {
    return (
        <div id="banner">
            <div id="banner-content">Book Worm</div>
            <div id="nav-bar">
                <a href="#login" onClick={() => handlePageChange('Login')} >
                    Login
                </a>
                <a href="#Book-Search" onClick={() => handlePageChange('BookSearch')} >
                    Book Search
                </a>
                <a href='#Manual-Entry' onClick={() => handlePageChange('Manualentry')} >
                    Manual Entry
                </a>
            </div>
        </div>
    )
}