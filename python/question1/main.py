"""
Question 1: Parse and Summarize Log Files

Problem:
Write a Python script that reads a server log file, extracts errors, and outputs a summary of errors grouped by error type and how many times each error occurred. Log lines follow this format:

```log
2024-09-18 12:35:22 ERROR ConnectionTimeout: Connection to database failed
2024-09-18 12:36:01 INFO Connection restored
2024-09-18 12:36:55 ERROR IOError: Unable to read file /etc/config.cfg
```
Requirements:
1. Parse the log file and find all lines that contain the word "ERROR."
2. Group errors by their error type (e.g., ConnectionTimeout, IOError) and count their occurrences.
3. Store the summary on to a database (sqlight setup function provided).
4. Output the summary as a dictionary
"""

import sqlite3

SQLITE_DATABASE_PATH = 'server.db'
LOG_FILE_PATH = 'server.log'


def _setup_database(database_path: str) -> None:
    """
    Set up the SQLite database for storing error summaries.
    Connect to the SQLite database (or create it if it doesn't exist)

    :param database_path: Path to the SQLite database.
    :return: None
    """

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS error_summary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TIMESTAMP,
            error_type VARCHAR(250),
            count INTEGER
        )
    ''')

    conn.commit()
    conn.close()


def save_to_database(summary: dict[str, int], database_path: str) -> None:
    """
    @DocString
    """
    pass


def summarise_errors(log_file_path: str) -> dict[str, int] | dict[None, None]:
    """
    @DocString
    """
    pass


if __name__ == "__main__":
    pass
