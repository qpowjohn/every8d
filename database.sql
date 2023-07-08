CREATE TABLE SMSLog (
  SN int NOT NULL AUTO_INCREMENT,
  BatchID varchar(36) DEFAULT NULL,
  mobile varchar(20) NOT NULL,
  Content nvarchar(max) NOT NULL,
  CreateTime datetime DEFAULT CURRENT_TIMESTAMP,
  UpdateTime datetime ON UPDATE CURRENT_TIMESTAMP,
  Status int DEFAULT NULL,
  PRIMARY KEY (SN)
);