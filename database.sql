CREATE TABLE SMSLog (
  SN int NOT NULL AUTO_INCREMENT,
  BatchID varchar(36) DEFAULT NULL,
  mobile varchar(20) NOT NULL,
  Content VARCHAR(4000) CHARACTER SET utf8 NOT NULL,
  CreateTime datetime DEFAULT CURRENT_TIMESTAMP,
  UpdateTime datetime ON UPDATE CURRENT_TIMESTAMP,
  Status int DEFAULT NULL,
  PRIMARY KEY (SN)
);