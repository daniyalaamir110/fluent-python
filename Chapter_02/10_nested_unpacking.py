import os
import sqlite3


def db_results_unpacking_example():
    """
    Database Results Unpacking Example

    This function demonstrates the use of unpacking to get the results from a database query.

    The database is created with a table `users` with columns `id`, `name`, and `age`.
    The table is populated with three records.
    The query fetches the name of the user with `id` equal to 1.
    The result is unpacked to get the name of the user.
    """
    db_path = os.path.join(os.path.dirname(__file__), "10_user_db.db")

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    cursor.executescript(
        """
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        );
        INSERT INTO users (name, age) 
        VALUES
        ('Alice', 25),
        ('Bob', 30),
        ('Charlie', 35);
        """
    )

    # The query must return a single row. We can use unpacking to get the user from
    # the result list. However, we have method `fetchone()` to get the single row,
    # but we can also use `fetchall()` and unpack the result.
    [user] = cursor.execute(
        """
        SELECT * FROM users
        WHERE id = 1
        """
    ).fetchall()

    print(f"The user with id 1 is {user}")

    # The query must return a single row, with a single column. We can make use of
    # nested unpacking to get the value of `name`.
    [[name]] = cursor.execute(
        """
        SELECT name FROM users
        WHERE id = 1
        """
    ).fetchall()

    print(f"The name of the user with id 1 is {name}")


if __name__ == "__main__":
    db_results_unpacking_example()
