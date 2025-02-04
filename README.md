# DJ-Test-Django-Web-App-for-Page-Visit-Counter
The DJ Test app is a Django-based web application that tracks the number of times a page has been visited. Every time you refresh the page, the visit count increases, and the updated count is displayed. Even when revisiting the page, the app continues to keep track of the total number of visits.

Features
Displays the number of visits to the page.
Increases the visit count on each refresh.
The visit count persists even when the page is revisited.
Built with Django framework and uses a virtual environment for project dependencies.
Technologies Used
Django: A high-level Python web framework.
SQLite: Database used for storing the visit count (default for Django).
Python: Programming language.
Virtual Environment (venv): Used to manage project dependencies.

# Set up Virtual Environment
Inside the project folder, create and activate a virtual environment:

# Create virtual environment
->python -m venv venv

# Activate virtual environment
->venv\Scripts\activate

# Install Dependencies
Once the virtual environment is activated, install the required dependencies:

->pip install -r requirements.txt

# Set up Database and Migrations
Run the following commands to set up your database and migrations:

# Apply migrations to set up the database
->python manage.py migrate
# Start the Development Server
After setting up everything, run the development server to see the app in action:

->python manage.py runserver

You can now visit http://127.0.0.1:8000/ to see the visit count in action!

# Folder Structure

![image](https://github.com/user-attachments/assets/e0140212-f6d6-4257-89ad-647bdf1be467)

# How It Works
1) Initial Visit: When a user first visits the page, the visit count is set to 1.

2) Subsequent Visits: Each time the page is refreshed or visited again, the visit count is incremented by 1 and displayed on the page.
   
3) Database: The visit count is stored in the database to persist the data across sessions, even if the server is restarted.
