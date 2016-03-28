# Flask Restful API Template with Mysql

### Install Mysql

`sudo apt-get install mysql-server-5.6`


### Install Required

```
sudo apt-get install python2
sudo apt-get install python-pip
sudo pip install virtualenv
```

In case Ubuntu  
`sudo apt-get install python-mysql.connector`

or 

In case Mac  
`brew install mysql-connector-python`


### Use Virtualenv

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```


### set environment

```
export APP_ORM_CONFIG=<mode>
export APP_DEVELOPMENT_DATABASE_URI=<mysql_uri>
```
* \<mode\> = 'production', 'development', 'testing', 'default'
* \<mysql_uri\> = `mysql://<username>:<password>@<hostname>/<database_name>`



### Create database at the first

`echo 'db.create_all()' | ./manage.py shell`


### Run server

`./manage.py runserver`


### Test Browser

Try `http://localhost:5000/api/v1/spaces`
