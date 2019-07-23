#!/bin/bash
mysql -h 35.226.222.111 -u praheja -pparulraheja <<MY_QUERY
USE praheja
delete from users where username like "test%"
