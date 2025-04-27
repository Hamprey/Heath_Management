Overview
This Health Information System provides a streamlined and secure platform for managing health programs 
and client data. It allows doctors to manage programs, register clients, enroll clients in multiple programs, 
and securely share client data through APIs.





Features
The project is able to Create, update, and manage health programs  like TB, HIV, Malaria.
The doctor is able register and track the client through registering clients with personal and health information.
The sytem allowa the doctor to nroll clients in multiple health programs thus its flexiable.
The system has advanced search and filtering to find clients by name, program, or condition.
The system allows the doctor to view and manage comprehensive client profiles.
The system allows the doctor to expose API intergration and safely expose client profiles to third-party systems.
The system allows scallabilty to be intergrated with other systems.


## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** PostgreSQL / SQLite
- **Authentication:** OAuth2 (for APIs) and Django REST Framework (DRF)
- **Version Control:** Git & GitHub


Approach & Design
Modular Architecture: Separating programs, clients, enrollments, and APIs into distinct modules.
Security First: Data encryption, API authentication, and role-based access control.
Scalable Database: Structured relationships for easy growth and maintenance.
(Detailed in Presentation)



Prototype Demonstration
A screen recording of the system in action is available through these link https://youtu.be/32NHca0A320

```
health_program/
├── health_program/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── health_system/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── __pycache__/
├── static/
│   └── core/
│       ├── script.js
│       └── style.css
├── templates/
│   └── core/
│       ├── add_program.html
│       ├── all_clients.html
│       ├── base.html
│       ├── client_profile.html
│       ├── enroll_client.html
│       ├── enrolled_clients.html
│       ├── index.html
│       └── register_client.html
├── venv/
├── db.sqlite3
└── manage.py
```


## How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Hamprey/Heath_Management.git
   ```

2. **Navigate into the Project Directory**
   ```bash
   cd Health_Program
   ```

3. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the Project Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Apply Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

---

Now you can access the project at `http://127.0.0.1:8000/` in your browser!



Contact
Developer: Hamprey Aganyo Ndemo
GitHub: @Hamprey
