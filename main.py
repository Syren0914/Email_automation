from datetime import date, timedelta  # core python module
import time
import pandas as pd  # pip install pandas

from send_email import send_email  


# Public GoogleSheets url - not secure!
SHEET_ID = "1pubXtXNQMhvrlooK-2yAMax2w820ZpnO2lVzSaPb-4I" 
SHEET_NAME = "sheet1"  
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


def load_df(url):
    parse_dates = ["due_date", "reminder_date"]
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df


def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present >= row["reminder_date"].date()) and (row["has_paid"] == "no"):
            send_email(
                subject=f'[Syren0914]',
                receiver_email=row["email"],
                name=row["name"],
                due_date=row["due_date"].strftime("%d, %b %Y"),  
                amount=row["amount"],
            )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"


while True:
    df = load_df(URL)
    result = query_data_and_send_emails(df)
    print(result)

    # Sleep for 24 hours before checking again
    time.sleep(24 * 60 * 60)  # Sleep for 24 hours