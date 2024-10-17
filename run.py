import subprocess
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
subprocess.Popen(['start', 'cmd', '/k', f'cd /d {current_dir} && python local.py'], shell=True)
subprocess.Popen(['start', 'cmd', '/k', f'cd /d {current_dir} && ngrok http 5000'], shell=True)
