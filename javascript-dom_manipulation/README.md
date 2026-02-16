# JavaScript DOM Manipulation

## Overview

This directory contains exercises and examples focused on **DOM (Document Object Model) manipulation** using vanilla JavaScript.

DOM manipulation allows selecting, updating, and dynamically changing HTML elements, attributes, styles, and content in the browser. It enables interactive behavior and dynamic page updates.

---

## Learning Focus

This module demonstrates how to:

* Select DOM elements using `getElementById`, `querySelector`, and `querySelectorAll`
* Modify element content using `textContent`, `innerHTML`, etc.
* Change element attributes and styles via JavaScript
* Create and remove DOM elements dynamically
* Attach event listeners for user interactions (clicks, input, etc.)
* Traverse and manipulate the DOM tree

---

## Example Snippet

```javascript
const title = document.getElementById("header-title");
title.textContent = "Welcome to DOM Manipulation!";
title.style.color = "blue";
```

This snippet selects an element and updates its text and style.

---


## Skills Demonstrated

* Interacting with the DOM tree and updating page content programmatically
* Responding to user actions such as clicks and input
* Building dynamic and interactive UI behavior using plain JavaScript
* Understanding the bridge between JavaScript and HTML structure

---

## Why This Matters

DOM manipulation is core to frontend development because:

* It enables building interactive user interfaces
* It forms the foundation for frameworks (React, Vue, Angular)
* It improves debugging and performance insights
* It expands what you can build without relying on external libraries

Mastering DOM manipulation prepares you for responsive and dynamic web applications beyond static HTML and CSS.
