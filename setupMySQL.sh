sudo /etc/init.d/mysql start
mysql -uroot -e "create database ask;"
mysql -uroot -e "grant all privileges on ask.* to 'box'@'localhost' with grant option;"
cd /home/box/web/ask
python manage.py makemigrations
python manage.py migrate

