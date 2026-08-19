# dvswitch-web-switcher
WEBPAGE THAT WILL LOAD FOR TALKGROUP SWITCHER
# DVSwitch DMR Web Switcher

A lightweight Python/Flask web interface for AllStarLink v3 nodes to quickly tune DMR talkgroups via DVSwitch.

## Features
- Clean dark-mode interface
- Runs directly on port `5000`
- Sanitized input validation for DMR talkgroup execution

## Installation & Setup

1. **Install requirements:**
   ```bash
   sudo apt update
   sudo apt install python3-flask -y
#Open port 5000 on the firewall (ASL3/Debian):
sudo firewall-cmd --add-port=5000/tcp --permanent
sudo firewall-cmd --reload

2.Allow DVSwitch sudo execution without password:
Run sudo visudo and append:
ALL ALL=(ALL) NOPASSWD: /opt/MMDVM_Bridge/dvswitch.sh

3. Run the application:
python3 app.py

Open your browser to: http://<your-ip>:5000

