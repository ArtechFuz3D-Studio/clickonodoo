<!-- # ! Branch 15.0 is currently broken, if you want to use v15.0, pull from dev, but be warned this branch is undergoing regular changes.

use these details for initial set up on v15

- email: admin
- password: admin
- ! change after installing -->

# ! Repo is undergoing maintainence. V15 is working

![image](https://user-images.githubusercontent.com/72121107/114523314-789a0100-9c44-11eb-996a-47d8224635c7.png)

# Clickonodoo

by clickonrefresh
[Join My Odoo Discord Community](https://discord.gg/46kKJ5VeHt)

# Odoo | Open HRMS | Base Accounting Kit | Python-Pandas

### [Odoo v14 Custom Docker Image Build Repository](https://github.com/clickonrefresh/clickonodoo/pkgs/container/clickonodoo)

Customised Odoo ce with Open HRMS and a Full accounting Kit available for install, Python Pandas preinstalled for use with HRMS.

Before installing third party modules, please see their relative dependency modules which must be installed prior to 3rd party module install.

---

# Run with:

```
chmod +x install.sh
```

```
./install.sh
```

or

``` 
bash install.sh 
```





<!-- # How to update this image via Dockerfile

Make sure your Dockerfile, entrypoint.sh, odoo.conf and wait-for-psql.py files are up to date with the latest (official Odoo docker repo)[https://github.com/odoo/docker]

## The following customizations must be included in the following files for customization:

### Dockerfile

```
python3-pandas \
```

...
....
...

# How to use this repo image

## Login to your respective container registry

`docker login <registry url>`

## Change directory into the Dockerfile location

`cd DockerBuild/14.0/`

## Build the image from the Dockerfile

`docker build -t ghcr.io/clickonrefresh/clickonodoo .`

### where -t is to tag the image, default is latest or main depending on container registry.

### the period at the end of the line is to specify that the Dockerfile be built from the current file path.

## Build the image with a different tag

`docker build -t ghcr.io/clickonrefresh/clickonodoo:dev .`
`docker build -t ghcr.io/clickonrefresh/clickonodoo:staging .`
`docker build -t ghcr.io/clickonrefresh/clickonodoo:14.0 .`

#### and so on

## Finally push your changes to the registry

`docker push ghcr.io/clickonrefresh/clickonodoo`
fails with bad credential setup

# How to scaffold a new app using docker

## Enter the container

`docker exec -u root -it <containerID> /bin/bash`

## Inside the container, run

`/usr/bin/odoo scaffold <yourappname> /mnt/extra-addons`

### If you have used this repo to create an app then your newly creted app will appear in the project folders under odo/addons. This external path has been mapped to /mnt/extra-addons inside the container.

## Now change the file permissions to allow editing

`sudo chown -R $USER:$USER <yourappname>` -->

<!-- https://docs.docker.com/engine/reference/commandline/login/#credentials-store -->

To Do
[] Update v15 dockerfile
[] build 13 and 15 and push to registry