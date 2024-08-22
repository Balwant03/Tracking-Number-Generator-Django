# Tracking-Number-Generator-Django
This is a Flask application that generates and manages unique tracking numbers. It leverages Redis for ensuring the uniqueness and scalability of the tracking numbers.

# Application setup
-- create virtualenv 
-- pip install django
-- pip install djangorestframework

# Migrate the Database:
-- python manage.py makemigrations
-- python manage.py migrate

# Run Application
-- python manage.py runserver

# API Call
curl --location 'http://localhost:8000/api/tracker/next-tracking-number?origin_country_id=INDIA&destination_country_id=IND&customer_id=001&weight=65.55&customer_name=Balwant&customer_slug=Kumar'

# Response

  {
      "tracking_number": "904303e17c92",
      "created_at": "2024-08-22T12:36:42.824389"
  }



