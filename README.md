# Table Booking Service (BE)

## Overview
An online platform enabling customers to search and book restaurant tables based on their location and available time slots. The service provides real-time availability and restaurant recommendations.

**Tech Stack for BE**:
Python, Flask, PostgreSQL, SQLAlchemy, Docker, AWS (ECS), AWS (RDS, PostgreSQL) 

**GitHub:** [Frontend](https://github.com/diakymenko/booking-service-front-end) | [Backend](https://github.com/diakymenko/table_booking_service) | [Demo](https://adaacademy.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=1e7a5db5-140e-4388-b862-aef501636909)

## Key Features
- Fetching restaurant data using the Yelp API to display restaurant names, types, images, and review ratings.  
- Determining the user's location through ipapi/ipify APIs and recommending nearby restaurants.  
- Enabling reservations by considering available time slots, table capacity, average dining duration, and preventing overbooking.  
- Implementing full CRUD functionality for Reservation and Restaurant models using Python, Flask, PostgreSQL, and SQLAlchemy.  
- Deploying the application with Docker and AWS (ECS, RDS).


## Dependencies:
alembic==1.5.4
attrs==21.2.0
autopep8==1.5.5
certifi==2020.12.5
chardet==4.0.0
click==7.1.2
Flask==1.1.2
Flask-Cors==3.0.10
Flask-Migrate==2.6.0
Flask-SQLAlchemy==2.4.4
gunicorn==20.1.0
idna==2.10
iniconfig==1.1.1
itsdangerous==1.1.0
Jinja2==2.11.3
Mako==1.1.4
MarkupSafe==1.1.1
packaging==20.9
pluggy==0.13.1
psycopg2-binary==2.9.1
py==1.10.0
pycodestyle==2.6.0
pyparsing==2.4.7
pytest==6.2.4
python-dateutil==2.8.1
python-dotenv==0.15.0
python-editor==1.0.4
requests==2.25.1
six==1.15.0
SQLAlchemy==1.3.23
toml==0.10.2
urllib3==1.26.4
Werkzeug==1.0.1

## Deployment
The service is deployed to AWS:
http://35.88.133.158/


