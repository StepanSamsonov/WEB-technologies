﻿sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf
sudo nginx -t
sudo /etc/init.d/nginx restart