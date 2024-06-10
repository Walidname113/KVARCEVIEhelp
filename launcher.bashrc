clear
cd && cd KVARCEVIEhelp
chmod +x update.py; update.sh; install.sh
pkg install python3 -y > /dev/null 2>&1
cd && cd KVARCEVIEhelp && python3 update.py