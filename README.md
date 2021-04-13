
clickonodoo
by clickonrefresh/countdocula
Odoo v14 Custom Docker Image Build Repository
Customised Odoo ce, Python Pandas preinstalled.
This repo is the 'github autobuild' for clickonrefresh/clickonodoo custom odoo ce docker image.
This image is a modified version of the latest Odoo v14 official docker image.
Run with docker-compose.yml:

version: '3'
services:
  web:
    container_name: odoo
    image: countdocula/clickonodoo:latest
    depends_on:
      - db
    ports:
      - 8069:8069
    volumes:
      - odoo-web-data:/var/lib/odoo
      - ./config:/etc/odoo
      - ./addons:/mnt/extra-addons
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo
      - APP_URL=customurl
    restart: always
  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_USER=odoo
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - odoo-db-data:/var/lib/postgresql/data/pgdata
volumes:
  odoo-web-data:
  odoo-db-data:

In your project root, create the following directories and files to run odoo with custom configurations and extra addons:

Create an odoo.conf and config directory

/myproject/config/odoo.conf

[options]
addons_path = /mnt/extra-addons
data_dir = /var/lib/odoo
; admin_passwd = admin
; csv_internal_sep = ,
; db_maxconn = 64
; db_name = False
; db_template = template1
; dbfilter = .*
; debug_mode = False
; email_from = False
; limit_memory_hard = 2684354560
; limit_memory_soft = 2147483648
; limit_request = 8192
; limit_time_cpu = 60
; limit_time_real = 120
; list_db = True
; log_db = False
; log_handler = [':INFO']
; log_level = info
; logfile = None
; longpolling_port = 8072
; max_cron_threads = 2
; osv_memory_age_limit = 1.0
; osv_memory_count_limit = False
; smtp_password = False
; smtp_port = 25
; smtp_server = localhost
; smtp_ssl = False
; smtp_user = False
; workers = 0
; xmlrpc = True
; xmlrpc_interface = 
; xmlrpc_port = 8069
; xmlrpcs = True
; xmlrpcs_interface = 
; xmlrpcs_port = 8071

and Create and addons folder where you can add extra modules and apps to.

/myproject/addons
