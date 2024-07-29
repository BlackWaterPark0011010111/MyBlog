# My Blog

My Blog is a blogging application written in Python using the Django framework. This application allows users to create, edit, delete, 
and view blog posts. The project includes user authentication features, an admin panel, and other capabilities.



## Description

The "My Blog" project provides users with the ability to maintain their own blog. The application supports basic features such as creating, editing, 
and deleting blog posts, as well as viewing all posts. The authentication system allows for user management and provides access to different features.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your_username/my-blog.git
    ```

2. Navigate to the project directory:

    ```sh
    cd my-blog
    ```

3. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # for Windows use `venv\Scripts\activate`
    ```

4. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

5. Apply the database migrations:

    ```sh
    python manage.py migrate
    ```

6. Create a `.env` file in the project root and add the necessary environment variables (see [Environment Variables](#environment-variables)).

## Usage

1. Start the development server:

    ```sh
    python manage.py runserver
    ```

2. Navigate to `http://127.0.0.1:8000/` in your web browser to see the blog in action.

3. Log in to the admin panel at `http://127.0.0.1:8000/admin` to manage blog content.

## Project Structure

- `manage.py`: The main file for managing the Django project.
- `connections.py`: A file for managing database connections.
- `db.sqlite3`: The SQLite database file.
- `.env`: A file for storing environment variables.
- `.gitignore`: A file specifying which files and folders should be ignored by Git.
- `requirements.txt`: A file containing project dependencies.
- `my_blog/`: Directory containing project settings and configurations.
  - `settings.py`: Django project settings.
  - `urls.py`: URL configuration.
  - `wsgi.py`: Entry point for WSGI-compatible web servers.
- `blog/`: Blog application.
  - `models.py`: Data model definitions.
  - `views.py`: Request handling logic.
  - `urls.py`: URL routes for the blog application.
  - `templates/`: Templates for rendering data.
  - `static/`: Static files (CSS, JavaScript, images).

## Environment Variables

To run the project, you need to create a `.env` file in the project root and add the following variables:
