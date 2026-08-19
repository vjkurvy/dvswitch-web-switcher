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
   sudo apt install python3-flask git -y

   Open port 5000 on the firewall (ASL3/Debian):

Bash
sudo firewall-cmd --add-port=5000/tcp --permanent
sudo firewall-cmd --reload
Allow DVSwitch sudo execution without password:
Run sudo visudo and append:

Plaintext
ALL ALL=(ALL) NOPASSWD: /opt/MMDVM_Bridge/dvswitch.sh
Clone and Run:

Bash
git clone [https://github.com/vjkurvy/dvswitch-web-switcher.git](https://github.com/vjkurvy/dvswitch-web-switcher.git)
cd dvswitch-web-switcher
python3 app.py
Open in your browser:

Plaintext
http://<your-pi-ip>:5000

4. Click **Commit changes...** in the top right.

---

### You're all set!
Your repository is completely functional and ready to be used or cloned onto any node.
