sudo /etc/init.d/mysql start
mysql -uroot -e "create database ask;"
mysql -uroot -e "grant all privileges on ask.* to 'box'@'localhost' with grant option;"


