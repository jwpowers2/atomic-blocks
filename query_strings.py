
create_branch = "CREATE TABLE IF NOT EXISTS branch (id SERIAL PRIMARY KEY,branch_name varchar(255),balance smallint);"
create_account =   """CREATE TABLE IF NOT EXISTS account 
                    (id SERIAL PRIMARY KEY,user_name varchar(255),balance numeric,branch_id int);"""

insert_branch = "INSERT INTO branch (branch_name, balance) VALUES ('BigBank', 0)"
insert_account_1 = "INSERT INTO account (user_name,balance,branch_id) VALUES ('Bob', 0, (SELECT id FROM branch WHERE branch_name='BigBank'));" 
insert_account_2 = "INSERT INTO account (user_name,balance,branch_id) VALUES ('Alice', 0, (SELECT id FROM branch WHERE branch_name='BigBank'));"

drop_account = "DROP TABLE IF EXISTS account;"
drop_branch = "DROP TABLE IF EXISTS branch;"

read_data_account = "SELECT * FROM account;"
read_data_branch = "SELECT * from branch;"

# begin -> commit makes a transaction in postgres
# if anything goes wrong, it automatically rolls everything back which has happened in the transaction block

update_good = """
BEGIN;
    UPDATE account SET balance = balance + 100.00 WHERE user_name = 'Alice';
    UPDATE branch SET balance = balance + 100 WHERE branch_name='BigBank';
    UPDATE account SET balance = balance + 100.00 WHERE user_name = 'Bob';
    UPDATE branch SET balance = balance + 100 WHERE branch_name='BigBank';
COMMIT;
"""

update_breaking = """
BEGIN;
    UPDATE account SET balance = balance + 100.00 WHERE user_name = 'Alice';
    UPDATE branch SET balance = balance + 100 WHERE branch_name='BigBank';
    UPDATE account SET balance = balance + 100.00 WHERE user_name = 'Bob';
    UPDATE branch SET balance = balance + 10000 WHERE branch_name='BigBank';
COMMIT;
"""