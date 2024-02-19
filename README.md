# DjangoRestFramework

# Invoices App

This is a simple Django application that allows you to create and manage invoices and their details.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.x
* Django 3.x
* Django Rest Framework
* pip

### Installing

1. Clone the repository

   git clone https://github.com/your_username/invoices_app.git
 

2. Create a virtual environment and activate it

   python -m venv env
   source env/bin/activate   # for Linux/Mac
   env\Scripts\activate      # for Windows


3. Install the dependencies

   pip install -r requirements.txt

4. Create a new Django project

   django-admin startproject invoices_project
 
5. Add the invoices app to the `INSTALLED_APPS` list in the `settings.py` file

     python
   INSTALLED_APPS = [
       
       'rest_framework',
       'invoices',
   ]


6. Run the migrations

   python manage.py migrate

7. Run the server

   python manage.py runserver


   ####OUTPUT VIDEO
   https://drive.google.com/file/d/14fW_tv4vJX6kDOhiiv9j133svzcCz_Of/view?usp=drivesdk
