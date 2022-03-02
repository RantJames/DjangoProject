Clone repo: git clone https://github.com/RantJames/DjangoProject.git

cd <directory_structure>\DjangoProject\
# install dependencies
pip install -r requirements.txt

# Update Database details in DjangoProject\classDemo\settings.py
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<database_name>,
        'HOST': <hostname>,
        'PORT': <database_port>,
        'USER': <username>,
        'PASSWORD': <password>
    }
# To perform migrations
python manage.py makemigrations
python manage.py migrate

# Run application
python manage.py runserver

# Application Url
http://127.0.0.1:8000/app/hotellist/

# POST json body

{
	"id":2,
	"name": "Garden Inn 2",
	"price": 250
}
