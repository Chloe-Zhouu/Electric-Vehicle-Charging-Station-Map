import sys

sys.path.insert(0, '/var/www/Electric-Vehicle-Charging-Station-Map')

activate_this = '/home/ubuntu/projects/APIC-Hackathon_2022/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app import app as application