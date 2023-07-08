import requests
import mysql.connector
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--uid", type=str, required=True, help="Every8D平台帳號")
parser.add_argument("-p", "--pwd", type=str, required=True, help="Every8D平台密碼")

args = parser.parse_args()

uid = args.uid
pwd = args.pwd

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="smsdb"
)

# Create a cursor object
cursor = db.cursor()

# Loop through the SMSLog table
while True:
    # Select the records that have a BatchID but no Status
    sql = "SELECT SN, BatchID FROM SMSLog WHERE BatchID IS NOT NULL AND Status IS NULL"
    cursor.execute(sql)
    records = cursor.fetchall()

    # For each record, send a POST request to the URL and get the Status
    for record in records:
        sn = record[0]
        batch_id = record[1]
        url = "https://api.e8d.tw/API21/HTTP/GetDeliveryStatus.ashx"
        data = {
            "UID": uid,
            "PWD": pwd,
            "BID": batch_id
        }
        response = requests.post(url, data=data)
        status = response.text

        # Update the Status in the SMSLog table
        sql = "UPDATE SMSLog SET Status = %s WHERE SN = %s"
        val = (status, sn)
        cursor.execute(sql, val)
        db.commit()

        time.sleep(1)

    # waiting for 30 second every loop, not too fast, maybe trigger 429 too many connetion.
    time.sleep(30)
