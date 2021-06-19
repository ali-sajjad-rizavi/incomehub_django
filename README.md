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
- Put a `secrets.json` file in the project root directory (the
  same folder where `manage.py` file exists). The structure of
  `secrets.json` (all secret information will be kept here)
  should be as follows:
```
{
    "AWS_RDS_POSTGRES_USER": "MyDbUser",
    "AWS_RDS_POSTGRES_PASSWORD": "*****",
    "AWS_RDS_POSTGRES_DB_HOST": "www.example.com",
    "AWS_ACCESS_KEY_ID": "ABC123",
    "AWS_SECRET_ACCESS_KEY": "*****",
    "AWS_STORAGE_BUCKET_NAME": "aws-s3-bucket-name"
}
```

- Now to run the server:
```
python manage.py runserver
```
Navigate to http://localhost:8000/ and you'll see the website homepage.
