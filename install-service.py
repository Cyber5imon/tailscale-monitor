import subprocess
import os

def setup_virtual_environment():
    subprocess.run(["python3", "-m", "venv", "."])
    subprocess.run(["bin/pip", "install", "tailscale", "notify2"])

def configure_systemd_service():
	username = os.getlogin()
	current_directory = os.getcwd()
    with open("~/.config/systemd/user/tailscale-monitor.service", "w") as f:
        f.write(f"""
[Unit]
Description=Tailscale Device Monitor
Documentation=https://github.com/Cyber5imon/tailscale-monitor

[Service]
User={username}
WorkingDirectory={current_directory}
ExecStartPre=/bin/bash -c "source bin/activate"
ExecStart=/usr/bin/python3 tailscale_monitor.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=default.target
        """)
    subprocess.run(["systemctl", "--user", "enable", "tailscale-monitor.service"])
    subprocess.run(["systemctl", "--user", "start", "tailscale-monitor.service"])

def main():
	if not os.path.exists("bin"):
	    setup_virtual_environment()
	if not os.path.exists("~/.config/systemd/user/tailscale-monitor.service"):
    	configure_systemd_service()

if __name__ == "__main__":
    main()
