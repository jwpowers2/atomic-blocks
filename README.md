# lesson on atomic block (batch) inserts

## lesson setup

- dockerfile for postgres DB
- sql script to create DB
- sql script to insert data
- sql script to update data ?  

## to run

### install psycopg2 python postgres library
### you can use a virtual env if you want (windows example below)

    python -m virtualenv env 
    cd env
    source Scripts/activate
    pip install psycopg2-binary


### spin up the postgres docker image using docker compose

### run the sql scripts to watch batch / atomic operations
### uses python script

- run the create-table script
- run the insert script
- run the read_data script
- run the update script
- run the read_data script
- run the bad_update script
- run the read_data script

