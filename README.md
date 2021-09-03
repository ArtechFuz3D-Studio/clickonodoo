![image](https://user-images.githubusercontent.com/72121107/114523314-789a0100-9c44-11eb-996a-47d8224635c7.png)

# Clickonodoo
   by clickonrefresh/countdocula
    
    
# Odoo | Open HRMS | Base Accounting Kit | Python-Pandas

### [Odoo v14 Custom Docker Image Build Repository](https://github.com/clickonrefresh/clickonodoo/pkgs/container/clickonodoo)
   Customised Odoo ce with Open HRMS and a Full accounting Kit available for install, Python Pandas preinstalled for use with HRMS.

   Before installing third party modules, please see their relative dependency modules which must be installed prior to 3rd party module install.

----------------------
# Run with:

```
bash install.sh
```

# [Join My Discord Server for Odoo Community Edition](https://discord.gg/kaVT7m9V4p)


# How to update this image via Dockerfile

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

``` docker login <registry url> ```

## Change directory into the Dockerfile location

``` cd DockerBuild/14.0/ ```

## Build the image from the Dockerfile

``` docker build -t ghcr.io/clickonrefresh/clickonodoo . ```

### where -t is to tag the image, default is latest or main depending on container registry.
### the period at the end of the line is to specify that the Dockerfile be built from the current file path.

## Build the image with a different tag

``` docker build -t ghcr.io/clickonrefresh/clickonodoo:dev . ```
``` docker build -t ghcr.io/clickonrefresh/clickonodoo:staging . ```
``` docker build -t ghcr.io/clickonrefresh/clickonodoo:14.0 . ```
#### and so on

## Finally push your changes to the registry
 
 ``` docker push ghcr.io/clickonrefresh/clickonodoo ```