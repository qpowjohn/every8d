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

# Loop through the SMSLog table
while True:
    # Connect to the database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="smsdb"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Select the records that have no BatchID
    sql = "SELECT SN, mobile, Content FROM SMSLog WHERE BatchID IS NULL"
    cursor.execute(sql)
    records = cursor.fetchall()

    # For each record, send a POST request to the URL and get the BatchID
    for record in records:
        sn = record[0]
        mobile = record[1]
        content = record[2]
        print ("Get Data, DEST: " + mobile + " MSG: " + content)
        url = "https://api.e8d.tw/API21/HTTP/sendSMS.ashx"
        data = {
            "UID": uid,
            "PWD": pwd,
            "DEST": mobile,
            "MSG": content
        }
        response = requests.post(url, data=data)
        result = response.text
        batch_id = result.split(",")[-1] # get guid
        
        # Update the BatchID in the SMSLog table
        sql = "UPDATE SMSLog SET BatchID = %s WHERE SN = %s"
        val = (batch_id, sn)
        cursor.execute(sql, val)
        db.commit()
        time.sleep(1)
    
    # waiting for 30 second every loop, not too fast, maybe trigger 429 too many connetion.
    time.sleep(30)