from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.smtp.hooks.smtp import SmtpHook
from datetime import datetime
import csv

class Wishes:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"""
        <html>
            <body>
                <h2>Happy Birthday {self.name}! 🎉🎂</h2>

                <p>
                    Wishing you a very Happy Birthday!
                </p>

                <p>
                    May your day be filled with happiness,
                    success, and wonderful moments.
                </p>

                <br>

                <p>
                    Best Wishes,<br>
                    Deepak
                </p>
            </body>
        </html>
        """


def get_employee_data():

    employees = []

    with open("Birthday_email_airflow/data/Birthday_Info.csv","r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            employees.append(row)

    return employees

employees = get_employee_data()

def check_birthdays(ti):

    today = datetime.now().strftime("%m-%d")

    birthday_employees = []

    for employee in employees:

        employee_birthday = datetime.strptime(
            employee["dob"],
            "%Y-%m-%d"
        ).strftime("%m-%d")

        if employee_birthday == today:

            birthday_employees.append({
                "name": employee["name"],
                "email": employee["email"]
            })

    ti.xcom_push(
        key="birthday_employees",
        value=birthday_employees
    )

    print(
        f"Birthday employees: {birthday_employees}"
    )


def send_birthday_emails(ti):

    birthday_employees = ti.xcom_pull(
        task_ids="check_birthdays",
        key="birthday_employees"
    )

    if not birthday_employees:
        print("No employee birthday today.")
        return

    with SmtpHook(
        smtp_conn_id="gmail-smtp"
    ) as smtp_hook:

        for employee in birthday_employees:

            wish = Wishes(
                employee["name"]
            )

            smtp_hook.send_email_smtp(
                to=employee["email"],
                subject=(
                    f"Happy Birthday "
                    f"{employee['name']}! 🎉"
                ),
                html_content=wish.greet()
            )

            print(
                f"Birthday email sent to "
                f"{employee['name']} "
                f"at {employee['email']}"
            )


with DAG(
    dag_id="daily_birthday_email_dag",

    start_date=datetime(2026, 1, 1),

    schedule="@daily",

    catchup=False,

    tags=[
        "birthday",
        "email",
        "xcom"
    ]

) as dag:

    check_birthday_task = PythonOperator(
        task_id="check_birthdays",
        python_callable=check_birthdays
    )

    send_email_task = PythonOperator(
        task_id="send_birthday_emails",
        python_callable=send_birthday_emails
    )


    check_birthday_task >> send_email_task