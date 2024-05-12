
---

# FastAPI Project README

## Description

This FastAPI project provides endpoints for managing users, posts, and comments. It includes functionalities like user sign up, login, post creation, retrieval, updating, deletion, comment creation, retrieval, updating, and deletion.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. Access the API documentation at `http://127.0.0.1:8000/docs` in your browser.

## Endpoints

### Users

- **GET /users**: Retrieve all users.
- **POST /signup**: Sign up a new user.
- **POST /login**: Log in a user.
- **PUT /users/{id}**: Update a user by ID.
- **DELETE /users/{id}**: Delete a user by ID.

### Posts

- **GET /post/**: Retrieve all posts.
- **POST /post/**: Create a new post.
- **PUT /post/{id}**: Update a post by ID.
- **DELETE /post/{id}**: Delete a post by ID.

### Comments

- **GET /post/comments/{id}**: Retrieve all comments for a post by post ID.
- **POST /post/comments/{id}**: Create a new comment for a post by post ID.
- **PUT /post/comments/{id_comm}**: Update a comment by comment ID.
- **DELETE /post/comments/{id_comm}**: Delete a comment by comment ID.

## Models

The project uses the following models:

- **User**: Represents a user with attributes like name, email, and password.
- **Post**: Represents a post with attributes like title, content, and author.
- **Comment**: Represents a comment with attributes like content, author, and post ID.

## Database

The project uses MongoDB as the database. Ensure MongoDB is running and accessible.

## Dependencies

The project dependencies are listed in the `requirements.txt` file.

---
