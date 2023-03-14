## Title : Online Calculator: v1.2

**Author: Abhishek Dey**

**Last Modified: 14/03/2023**

## Functionality added in v1.2:

* Inclusion of saving front end data into mysql table

## Installations:

* Flask

```
pip3 install flask

```

* Flask MySQL

```
sudo apt-get install libmysqlclient-dev

pip3 install flask_mysqldb

```

## Pre-requisite:


* Mysql Database **calculator_database**

* **calculator_table** Table should be already created in the database


```

mysql> describe calculator_table;
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| sl_no     | int         | NO   | PRI | NULL    | auto_increment |
| operation | varchar(30) | YES  |     | NULL    |                |
| num1      | float       | YES  |     | NULL    |                |
| num2      | float       | YES  |     | NULL    |                |
| result    | float       | YES  |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
5 rows in set (0.02 sec)


```


## Changes to be made in app.py

* change the mysql configuration as per your database created

```
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'calculator_database'

```

## Running the app:


```

python3 app.py

```
