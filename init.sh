git config --global user.name StepanSamsonov
git config --global user.email mynameisericlensherr@gmail.com
pip install gunicorn
ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/gunicorn.py /etc/gunicorn.d/gunicorn.py

gunicorn hello:wsgi_hello
