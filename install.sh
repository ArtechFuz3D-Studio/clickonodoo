sudo apt-get update \
  && sudo apt-get install zip -y \
  && sudo apt-get install curl -y \
  && sudo apt-get install wget -y \
  && sudo apt-get update

# Install Node via Node Version Manager
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
# run these commands to startup nvm
export NVM_DIR="$HOME/.nvm" 
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
# Install Node --lts version
nvm install --lts

# Install Docker
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce
# sudo systemctl status docker
sudo usermod -aG docker ${USER}



# Install Docker-Compose
mkdir -p ~/.docker/cli-plugins/ \
  && curl -SL https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose \
  && chmod +x ~/.docker/cli-plugins/docker-compose \
  && sudo chown $USER /var/run/docker.sock

# # Run Nginx
# cd Apps \
#   && cd nginx \
#   && docker-compose up -d \
#   && cd ..

# # Run Odoo
# cd Apps \
#   && cd odoo \
#   && docker-compose up -d \
#   && cd ..

# # Run Noip-DUC
# cd /opt \
#   && sudo mkdir noip && cd noip \
#   && sudo wget https://github.com/clickonrefresh/Automate-Noip-DUC/archive/main.zip \
#   && sudo unzip main.zip \
#   && cd Automate-Noip-DUC-main \
#   && sudo bash noip-duc.sh

# # Clean Up
# sudo apt-get update \
#   && sudo apt-get autoremove -y
