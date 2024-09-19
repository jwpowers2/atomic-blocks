# lesson on atomic block (batch) inserts

## lesson setup

### what you'll need:

1. docker / docker compose (comes with it these days)

2. python 

3. python virtual env, or you'll be installing globally 

### project setup

- install psycopg2 python postgres library

### you can use a virtual env if you want (windows example below)

    python -m virtualenv env 
    cd env
    source Scripts/activate
    pip install psycopg2-binary


### spin up the postgres docker image using docker compose

- from project root

    docker compose up --build

### for the demo, run the main.py file which will show a failed batch transaction

1. drop tables, make new users and bank branches
2. insert starting data into those tables
3. perform successful batch update of the account and bank branch data
3. perform failing batch update of the account and bank branch data

### how this shows batch transactions ?

- when the last transaction fails, the initial updates to user accounts also fail

