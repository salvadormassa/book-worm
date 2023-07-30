import React from "react";

export default function ManualEntry() {
    return (
        <div id="manual-entry">
            <form id="manual-entry-form">
                <div id="box-1">
                <label for="isbn">ISBN:</label>
                <input type="text" id="isbn" name="=isbn" />
                <label for="title">Title:</label>
                <input type="text" id="title" name="title" />
                <label for="authors">Author(s):</label>
                <input type="text" id="authors" name="authors" />
                </div>
                <div id="box-2">
                <label for="description">Description:</label>
                <textarea id="description" name="description" rows={5} cols={50}/>
                </div>
                <div id="box-3">
                <label for="publisher">Publisher:</label>
                <input type="text" id="publisher" name="publisher" />
                <label type="published-date">Published Date:</label>
                <input type="date" id="published-date" name="published-date" />
                {/* Genre add new genre */}
                <label for="genre">Genre</label>
                <input type="text" id="genre" name="genre" />
                </div>
                <div id="box-4">
                <label for="language">Language</label>
                <input type="text" id="language" name="language" />
                <label for="page-count">Page Count</label>
                <input type="text" id="page-count" name="page-count" />
                <label for="dust-jacket">Dust Jacket?</label>
                <input type="checkbox" id="dust-jacket" name="dust-jacket" />
                <label for="format">Format:</label>
                <select name="format" id="format">
                    <option value={"hardcover"}>Hardcover</option>
                    <option value={"paperback"}>Paperback</option>
                    <option value={"other"}>Other</option>
                </select>
                <label for="condition">Condition</label>
                <select name="condition" id="condition">
                    <option value={"like-new"}>Like New</option>
                    <option value={"fine"}>Fine</option>
                    <option value={"near-fine"}>Near Fine</option>
                    <option value={"very-fine"}>Like New</option>
                    <option value={"good"}>Good</option>
                    <option value={"fair"}>fair</option>
                    <option value={"poor"}>Poor</option>
                </select>
                </div>
                <div id="box-5">
                <label for="msrp">MSRP</label>
                <input type="text" id="msrp" name="msrp" />
                <label for="used-price">Our Price</label>
                <input type="text" id="used-price" name="used-price" />
                </div>
            </form>
        </div>
    )
};