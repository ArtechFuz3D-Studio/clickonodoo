sudo apt-get update
sudo apt-get install zip -y
sudo apt-get install curl -y
sudo apt-get install wget -y
sudo apt-get update
     
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common -y
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt-get update
sudo apt install docker-ce -y
sudo usermod -aG docker ${USER}
su - ${USER}

sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo apt-get update
     
cd ..
sudo docker-compose up -d


cd /opt
sudo mkdir noip && cd noip
sudo wget https://github.com/clickonrefresh/Automate-Noip-DUC/archive/main.zip
sudo unzip main.zip
cd Automate-Noip-DUC-main
sudo bash noip-duc.sh

sudo apt-get update
sudo apt-get autoremove -y

