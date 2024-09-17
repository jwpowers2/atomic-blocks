BEGIN
    SAVEPOINT  start_tran;
    UPDATE accounts SET balance = balance - 100.00 WHERE user_name = 'Alice';
    UPDATE branches SET balance = balance - 100.00 
        WHERE user_name = (SELECT branch_name FROM accounts WHERE user_name = 'Alice');
    UPDATE accounts SET balance = balance - 100 WHERE user_name = 'Bob';
    UPDATE branches SET balance = balance - 100.00 
        WHERE user_name = (SELECT branch_name FROM accounts WHERE user_name = 'Bob');
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK to start_tran;
        RAISE;
COMMIT;