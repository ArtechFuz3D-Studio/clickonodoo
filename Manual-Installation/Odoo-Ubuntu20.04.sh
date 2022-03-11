# Install Dependencies
sudo apt update
sudo apt install -y git python3-pip build-essential wget python3-dev python3-venv \
  && sudo apt install -y python3-wheel libfreetype6-dev libxml2-dev libzip-dev libldap2-dev libsasl2-dev \
  && sudo apt install -y python3-setuptools node-less libjpeg-dev zlib1g-dev libpq-dev \
  && sudo apt install -y libxslt1-dev libldap2-dev libtiff5-dev libjpeg8-dev libopenjp2-7-dev \
  && sudo apt install -y liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev

# Creating a System User
sudo useradd -m -d /opt/odoo15 -U -r -s /bin/bash odoo15

# Install Postgresql
sudo apt install postgresql
sudo su - postgres -c "createuser -s odoo15"

sudo wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb
sudo apt install ./wkhtmltox_0.12.5-1.bionic_amd64.deb

sudo su - odoo15
git clone https://www.github.com/odoo/odoo --depth 1 --branch 15.0 /opt/odoo15/odoo

cd /opt/odoo15
python3 -m venv odoo-venv

source odoo-venv/bin/activate

pip3 install wheel
pip3 install -r odoo/requirements.txt
deactivate

mkdir /opt/odoo15/odoo-custom-addons


exit

# sudo nano /etc/odoo15.conf
sudo cp odoo15.conf /etc/odoo15.conf

# [options]
# ; This is the password that allows database operations:
# admin_passwd = my_admin_passwd
# db_host = False
# db_port = False
# db_user = odoo15
# db_password = False
# addons_path = /opt/odoo15/odoo/addons,/opt/odoo15/odoo-custom-addons


# sudo nano /etc/systemd/system/odoo15.service
sudo cp odoo15.service /etc/systemd/system/odoo15.service

# [Unit]
# Description=Odoo15
# Requires=postgresql.service
# After=network.target postgresql.service

# [Service]
# Type=simple
# SyslogIdentifier=odoo15
# PermissionsStartOnly=true
# User=odoo15
# Group=odoo15
# ExecStart=/opt/odoo15/odoo-venv/bin/python3 /opt/odoo15/odoo/odoo-bin -c /etc/odoo15.conf
# StandardOutput=journal+console

# [Install]
# WantedBy=multi-user.target


sudo systemctl daemon-reload
sudo systemctl enable --now odoo15
sudo systemctl status odoo15
# sudo journalctl -u odoo15


sudo apt update
sudo apt install nginx -y
sudo apt install ufw -y
sudo ufw allow 'Nginx Full'
# sudo nano /etc/nginx/sites-enabled/example.com.conf
sudo cp example.com.conf /etc/nginx/sites-enabled/example.com.conf


# # Odoo servers
# upstream odoo {
#  server 127.0.0.1:8069;
# }

# upstream odoochat {
#  server 127.0.0.1:8072;
# }

# # HTTP -> HTTPS
# server {
#     listen 80;
#     server_name www.example.com example.com;

#     include snippets/letsencrypt.conf;
#     return 301 https://example.com$request_uri;
# }

# # WWW -> NON WWW
# server {
#     listen 443 ssl http2;
#     server_name www.example.com;

#     ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
#     ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
#     ssl_trusted_certificate /etc/letsencrypt/live/example.com/chain.pem;
#     include snippets/ssl.conf;
#     include snippets/letsencrypt.conf;

#     return 301 https://example.com$request_uri;
# }

# server {
#     listen 443 ssl http2;
#     server_name example.com;

#     proxy_read_timeout 720s;
#     proxy_connect_timeout 720s;
#     proxy_send_timeout 720s;

#     # Proxy headers
#     proxy_set_header X-Forwarded-Host $host;
#     proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#     proxy_set_header X-Forwarded-Proto $scheme;
#     proxy_set_header X-Real-IP $remote_addr;

#     # SSL parameters
#     ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
#     ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
#     ssl_trusted_certificate /etc/letsencrypt/live/example.com/chain.pem;
#     include snippets/ssl.conf;
#     include snippets/letsencrypt.conf;

#     # log files
#     access_log /var/log/nginx/odoo.access.log;
#     error_log /var/log/nginx/odoo.error.log;

#     # Handle longpoll requests
#     location /longpolling {
#         proxy_pass http://odoochat;
#     }

#     # Handle / requests
#     location / {
#        proxy_redirect off;
#        proxy_pass http://odoo;
#     }

#     # Cache static files
#     location ~* /web/static/ {
#         proxy_cache_valid 200 90m;
#         proxy_buffering on;
#         expires 864000;
#         proxy_pass http://odoo;
#     }

#     # Gzip
#     gzip_types text/css text/less text/plain text/xml application/xml application/json application/javascript;
#     gzip on;
# }


sudo systemctl restart nginx

# /etc/odoo15.conf
# proxy_mode = True


sudo systemctl restart odoo15

# /etc/odoo15.conf
# xmlrpc_interface = 127.0.0.1
# netrpc_interface = 127.0.0.1



# Multiproccessing mode
/etc/odoo15.conf
limit_memory_hard = 2684354560
limit_memory_soft = 2147483648
limit_request = 8192
limit_time_cpu = 600
limit_time_real = 1200
max_cron_threads = 1
workers = 5

sudo systemctl restart odoo15
