from flask import Flask
import psycopg2

app = Flask(__name__)

# Replace these database connection parameters with your actual values
db_params = {
    'dbname': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword',
    'host': 'db',
    'port': 5432
}

def query_database():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # Example query: Fetch the PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()

        # Close communication with the PostgreSQL database
        cursor.close()
        connection.close()

        return record

    except (Exception, psycopg2.Error) as error:
        return f"Error querying the database: {error}"

@app.route('/')
def hello_world():
    # Query the database and display the result in the response
    result = query_database()
    return f'Hello, Docker Compose with Nginx and PostgreSQL!<br>Database Version: {result}'

if __name__ == '__main__':
    # Run the Flask app on host '0.0.0.0' to make it accessible externally
    app.run(host='0.0.0.0', port=5000)
