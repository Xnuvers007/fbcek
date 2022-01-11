# linux Install

# dont forget to sudo su

pkg upgrade -y && pkg update -y  
apt update -y && apt full-upgrade -y
pkg install python3 -y && sudo apt install python3-pip
pip3 install -r requirements.txt
