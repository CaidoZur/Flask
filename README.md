## Project Overview
This project is a simple web application built using Flask, a micro web framework for Python. The application interacts with a MySQL database to perform CRUD (Create, Read, Update, Delete). The main functionalities of this application include:

1. Displaying a list of actors.
2. Adding a new actor.
3. Updating an existing actor's information.
4. Deleting an actor.

## Installation Instructions

### Prerequisites

- Python 
- MySQL
- Pip (Python package installer)

### Steps

1. **Clone the repository:**

    git clone https://github.com/your-repository-url.git

2. **Create a virtual environment:**

    python3 -m venv venv

3. **Install the required packages:**

    pip install flask flask-mysqldb

4. **Configure the MySQL database:**

   - Ensure MySQL is installed and running.
   - Create a database depending on the name you used.
   - Update the database configuration in the `api.py` file if needed (e.g., MySQL credentials).

5. **Run the application:**

    python app.py

   The application will start running on `http://127.0.0.1:5000`.

## Additional Information

API Usage
The application provides several routes for interacting with the actor table:

GET /: Fetches and displays all actors.
POST /add: Adds a new actor to the database. Expects form data with first_name and last_name.
GET /actors/<int:id>: Fetches a specific actor's details for updating.
POST /actors/<int:id>: Updates an actor's details in the database. Expects form data with first_name and last_name.
GET /delete/<int:id>: Deletes a specific actor from the database.