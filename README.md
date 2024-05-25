## Installation Instructions

### Prerequisites

- Python 
- MySQL
- Pip (Python package installer)

### Steps

1. **Clone the repository (If you are not using Github Desktop):**

    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```sh
    pip install flask flask-mysqldb
    ```

4. **Configure the MySQL database:**

   - Ensure MySQL is installed and running.
   - Create a database depending on the name you used.
   - Update the database configuration in the `app.py` file if needed (e.g., MySQL credentials).

5. **Run the application:**

    ```sh
    python app.py
    ```

   The application will start running on `http://127.0.0.1:5000`.