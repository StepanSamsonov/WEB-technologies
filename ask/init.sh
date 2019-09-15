git config --global user.name StepanSamsonov
git config --global user.email mynameisericlensherr@gmail.com
pip install --upgrade pip
pip install --upgrade django
pip install gunicorn

sudo ln -sf /home/box/web/ask/etc/nginx.conf /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart

sudo ln -sf /home/box/web/ask/etc/gunicorn.py /etc/gunicorn.d/gunicorn.py

cd /home/box/web/ask
gunicorn ask.wsgi:application
