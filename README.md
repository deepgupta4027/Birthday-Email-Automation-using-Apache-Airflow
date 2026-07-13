# Birthday Email Automation using Apache Airflow

This project automatically checks employee birthdays every day and sends personalized birthday emails using Gmail SMTP.

It demonstrates the use of Apache Airflow for workflow automation, task scheduling, XCom communication, and email integration.

# Features

- Daily scheduled Airflow DAG
- Reads employee birthday data
- Checks today's birthdays
- Uses XCom Push & Pull for task communication
- Sends personalized HTML emails using Gmail SMTP
- Modular Python code

## Technologies Used

- Python
- Apache Airflow
- Gmail SMTP
- XCom
- PythonOperator

##  Project Structure

```
birthday-email-airflow/
│
├── dags/
│   └── Birthday_wishes.py
├── data/
│   └── employees.csv
├── Screenshots/
      ├──  Screenshot 2026-07-13 131800.png
      ├──  Screenshot 2026-07-13 131943.png
      ├──  Screenshot 2026-07-13 132428.png
├── README.md
├── requirements.txt
└── .gitignore
```

## Workflow

```
Employee Data
      │
      ▼
Check Birthdays
      │
      ▼
XCom Push
      │
      ▼
Send Birthday Emails
      │
      ▼
Employee Inbox
```
## How to Run
1. Install Apache Airflow.
2. Install the SMTP provider.
3. Configure the Gmail SMTP connection in Airflow.
4. Copy the DAG into the `dags` folder.
5. Start Airflow.
6. Trigger the DAG or wait for the scheduled run.

## Screenshots
- Airflow Graph View
- Successful DAG Run
- Email received in Gmail


## Author

*Deepak Gupta*

Data Engineering | Apache Airflow | PySpark | 
