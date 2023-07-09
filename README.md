# 環境設置

if using MySQL 8

```
pip3 uninstall mysql-connector
pip3 install mysql-connector-python

```

# 如何使用

利用mysql，建立一Database，命名為smsdb，執行以下語法加入TABLE

```
mysql -uroot -p'password' smsdb < database.sql
```

您只需要將要發送的資料寫進此table，參考如下

```
INSERT INTO SMSLog (mobile, Content)
VALUES ('0912345678', '你好，這是一則測試簡訊');
```

執行發送簡訊，此排程會每秒鐘發送一筆簡訊，每30秒檢查一次資料庫
```
python sendSMS.py --uid account --pwd password
```

執行簡訊狀態檢查，此排程會每秒鐘檢查一筆簡訊，每30秒檢查一次資料庫
```
python GetDeliveryStatus.py --uid account --pwd password
```