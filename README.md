# incomehub_django
My final year project, a website where people can
find jobs, post jobs, and do more.
- Front end with Bootstrap
- Backend with Django3
- Cloud database: Amazon RDS for PostgreSQL (AWS)
- Media file cloud uploads: AWS S3 Bucket

### Members:
- Sayyid Ali Sajjad Rizavi ( BCSF17M555 )
- Syeda Maryam Imran Rizvi ( BITF17A053 )
- Umar Abdullah ( BCSF17M553 )

### How to setup the project? (For Windows)
- Clone the repository, create a virtual environment, and install
necessary requirements.
```
git clone git@github.com:ali-sajjad-rizavi/incomehub_django.git
cd incomehub_django
python -m venv venv
.\venv\scripts\activate.bat
pip install -r requirements.txt
```
- Set the following environment variables:
```
INCOMEHUB_DJANGO_SECRET_KEY = "*****"
AWS_RDS_POSTGRES_PASSWORD = "*****"
AWS_SECRET_ACCESS_KEY = "*****"
```

- Now to run the server:
```
python manage.py runserver
```
Navigate to http://localhost:8000/ and you'll see the website homepage.
