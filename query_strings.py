create_accounts = "CREATE TABLE IF NOT EXISTS accounts (user_name varchar(255),balance numeric);"
create_branches = "CREATE TABLE IF NOT EXISTS branches (user_name varchar(255),balance int);"

insert_accounts = "INSERT INTO accounts (user_name, balance) VALUES ('Bob', 0);" 
insert_branches = "INSERT INTO branches (user_name, balance) VALUES ('Alice', 0);"

read_data_accounts = "SELECT * FROM accounts;"
read_data_branches = "SELECT * from branches;"

update_good = """BEGIN 
    SAVEPOINT  start_tran;
    UPDATE accounts SET balance = balance - 100.00 WHERE user_name = 'Alice';
    UPDATE branches SET balance = balance - 100 
        WHERE user_name = (SELECT branch_name FROM accounts WHERE user_name = 'Alice');
    UPDATE accounts SET balance = balance - 100.00 WHERE user_name = 'Bob';
    UPDATE branches SET balance = balance - 100 
        WHERE user_name = (SELECT branch_name FROM accounts WHERE user_name = 'Bob');
    EXCEPTION
        WHEN OTHERS THEN
            ROLLBACK to start_tran;
            RAISE;
END;"""

update_breaking = "BEGIN\
    SAVEPOINT  start_tran;\
    UPDATE accounts SET balance = balance - 100.00 WHERE user_name = 'Alice';\
    UPDATE branches SET balance = balance - 100.00 \
        WHERE user_name = (SELECT branch_name FROM accounts WHERE user_name = 'Alice');\
    UPDATE accounts SET balance = balance - 100.00 WHERE user_name = 'Bob';\
    UPDATE branches SET balance = balance - 100.00 \
        WHERE user_name = (SELECT branch_name FROM accounts WHERE user_name = 'Bob');\
EXCEPTION\
    WHEN OTHERS THEN\
        ROLLBACK to start_tran;\
        RAISE;\
COMMIT;"