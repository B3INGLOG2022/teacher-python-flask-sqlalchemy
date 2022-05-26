## Sample : Flask with SQLAlchemy

This is a sample application to demonstrate the usage of an ORM library. 

It's a simple app using the Flask framework with the SQLAlchemy (ORM) and Alembic (for migrations) libraries. 
## Start the application 
```
docker-compose up -d
```
Connect to http://localhost:8001

**OR**

```
pip install -r requirements.txt
flask run
```
Connect to http://localhost:8000

## Init database
```
flask db upgrade
```

## Documentation links 
[Flask documentation](https://flask.palletsprojects.com/en/2.1.x/)

[Flask SQL Alchemy documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

[Flask migrate documentation](https://flask-migrate.readthedocs.io/en/latest/)
