# Query Engine

Django project exposing a dataset by a single GET API with a custom Django query engine that performs aggregation, filteration and sorting.
Operations are automatically detected based on URL operators and parameters of GET API.

## Getting Started

> Made using Django, Postgresql

### Prerequisites

What things you need to install the software and how to install them
```
Pipenv (Optional https://docs.pipenv.org/en/latest/)
Django==2.2.3
psycopg2==2.8.3
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
$ pip install --user pipenv (optional, pip only would work just fine)
$ pipenv install
```

### Setting Up
Set up data and migrations

```
$ pipenv shell (virtualenv)
$ cd adjust/adjust
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py shell
>>> from adjust_api.utils import insert_data
>>> insert_data()
```


End with an example of getting some data out of the system or using it for a little demo

## APIs 
 
 1.   Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.
```
   v1/analytics?date_to=2017-06-01&values=channel,country&sum=impressions,clicks&sortby=clicks

```
2.  Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
```        
   v1/analytics?date_from=2017-05-01&os=ios&values=date&sum=installs&sortby=date
 ``` 
3.  Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
```
   v1/analytics?date=2017-06-01&country=us&values=os&sum=revenue&sortby=revenue
```
4.  Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.
```
   v1/analytics?country=ca&values=channel&sum=cpi&sortby=cpi

```
### How does it works?
> Get queries have a certain structure associated which is associated with Django ORM.

###### Filters
 ```
os=ios
country=CA
date_to=2017-06-01

```
###### Values (comma seprated list)
 ```
values=channel,country
```
###### Aggregations 
 ```
sum = impressions,clicks
count = impressions
avg = revenue

```
###### Orderby
```
sortby = revenue
order = - (for ascending)
```

### Tests
###### TODO: Adding more test cases
```
python manage.py tests
```

### Authors

**Anshul**

