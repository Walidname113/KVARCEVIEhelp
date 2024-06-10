sed -i 's/\r$//' launcher.bashrc
chmod +x update.py; update.sh; install.sh > /dev/null 2>&1
pkg install python3 -y > /dev/null 2>&1
cd && cd KVARCEVIEhelp && python3 update.py
