git config --global user.name StepanSamsonov
git config --global user.email mynameisericlensherr@gmail.com
pip install gunicorn
ln -sf /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf
/etc/init.d/nginx restart

# cd /home/box/web
# sudo gunicorn -c /home/box/web/etc/gunicorn.py hello:wsgi_hello
cd /home/box/web/ask
sudo gunicorn -c /home/box/web/etc/gunicorn-django.py ask.wsgi:application

