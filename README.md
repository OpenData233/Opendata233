# Opendata233

OpenData233 is a non partisan project. We aim to keep an eye on Election 2016 to promote greater public voice and enhance public participation in politics



## How to Use

To use this project, follow these steps:

1. Create your working environment recommend using a  virtualenv( `$ virtualenv -p python3.4 --no-site-packages env`)
2. ` $ git init`
3. clone this project ` $ git clone https://github.com/OpenData233/Opendata233.git `
4. open the settings.py file in #Odata/settings.py
5.  Create and enter a secret key
6. Do your database setup (preferably postgres)
7. Install project requirements by running `$ pip install -r requirements.txt`
8. Prepare for migration ` $ ./manage.py makemigrations`
9. Migrate `$ ./manage.py migrate`
10.Create and account to access the admin `$ ./manage.py createsuperuser`
11. Run `$ python manage.py runserver` 




## To test Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)

## Project url

- [Open Data 233 Url](http://www.opendata233.com/)
