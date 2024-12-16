**README.md**

# Django Project Setup

This repository contains a basic Django project setup. Follow the instructions below to set up the project locally.

---

## **Project Structure**
The repository contains the following:
- A Django project initialized with a virtual environment.
- A `.gitignore` file to exclude unnecessary files from version control.
- An `initial app` for the project.
  
---

## **Setup Instructions**

### 1. **Clone the Repository**
Start by cloning this repository to your local machine:
```bash
https://github.com/abel-hak/Social-Media-Api.git
```

---

### 2. **Create a Virtual Environment**
Ensure that Python is installed (version 3.8+ recommended). Set up a virtual environment:
```bash
python -m venv venv
```

Activate the virtual environment:
- On Windows:
    ```bash
    venv\Scripts\activate
    ```
- On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

---

### 3. **Install Dependencies**
Install the required packages, including Django:
```bash
pip install -r requirements.txt
```

If a `requirements.txt` is not provided yet, you can generate it using:
```bash
pip freeze > requirements.txt
```

---

### 4. **Run the Django Project**
Perform the initial migration and run the development server:
```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to confirm the project is running.

---

### 5. **Create Superuser (Optional)**
To access the Django admin panel:
```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin user.

---

### 6. **Initial App**
An initial app has been set up. Add additional apps as needed using:
```bash
python manage.py startapp <app_name>
```

---

## **Project Guidelines**
- Keep the project modular with multiple apps.
- Follow Django best practices.
- Update `requirements.txt` after adding new dependencies.
- Commit frequently and push changes to the repository.

---

## **Contributing**
Feel free to fork the repository and submit a pull request for improvements or fixes.
