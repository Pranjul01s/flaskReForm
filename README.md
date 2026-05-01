# Flask Registration Form

A simple Flask web application that provides a user registration form with form submission and success confirmation.

## Project Structure

```
flaskassignment/
├── reform.py           # Main Flask application
├── templates/
│   ├── form.html       # Registration form page
│   └── success.html    # Success confirmation page
└── README.md           # Project documentation
```

## Features

- **Registration Form**: Collects user information including:
  - Full Name
  - Email
  - Username
  - Password

- **Form Submission**: POST method to handle form data submission
- **Success Page**: Displays submitted user information in a formatted table with submission timestamp
- **Bootstrap Styling**: Responsive design using Bootstrap 5.3.8 CSS framework

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone or download the project
2. Install Flask:
   ```bash
   pip install flask
   ```

## Running the Application

1. Navigate to the project directory:
   ```bash
   cd flaskassignment
   ```

2. Run the Flask application:
   ```bash
   python reform.py
   ```

3. Open your web browser and go to:
   ```
   http://localhost:5000
   ```

## Usage

1. Fill out the registration form with your information
2. Click the submit button
3. View your submitted information on the success page

## Routes

- **`/`** - Displays the registration form
- **`/registered`** - Handles form submission (POST/GET) and displays success page

## File Descriptions

### reform.py
Main Flask application file that:
- Initialises the Flask app
- Defines routes for the form and registration pages
- Handles form data submission and passes it to the success template

### templates/form.html
Registration form page featuring:
- Bootstrap styling for a clean, centred layout
- Input fields for fullname, email, username, and password
- Form submission to the `/registered` endpoint

### templates/success.html
Success confirmation page that:
- Displays submitted user data in a table format
- Shows the timestamp of form submission
- Uses Bootstrap for consistent styling

## Notes

- The application runs in debug mode by default
- All form data is passed via POST request and displayed on the success page
- No data persistence (database) is currently implemented
