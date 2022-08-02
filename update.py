# This script's purpose is to update the /bin/compile file with the latest Firefox & Geckodriver versions.

import os
import datetime
import time
import requests
from dotenv import load_dotenv
load_dotenv()

scriptPath = os.path.join(os.getcwd(), 'bin', 'compile')
latestFFVer = requests.get(
    "https://product-details.mozilla.org/1.0/firefox_versions.json").json()['LATEST_FIREFOX_VERSION']
latestgeckoVer = requests.get(
    "https://api.github.com/repos/mozilla/geckodriver/releases").json()[0]['name']
supportedHeroku = list(filter(lambda x: x.startswith("heroku"), list(map(
    lambda x: x['stack']['name'].lower(), requests.get(os.environ.get("GH_URL")).json()['data']))))


with open(scriptPath) as f:
    data = f.readlines()
data[2] = f"# Last updated: {datetime.datetime.strftime(datetime.datetime.now(), '%B %d, %Y %I:%M %p %z')}{time.tzname[time.daylight]}\n"
data[38] = f"VERSION_FIREFOX={latestFFVer}\n"
data[39] = f"VERSION_GECKODRIVER={latestgeckoVer}\n"
data[53] = '  "' + '" | "'.join(supportedHeroku) + '")\n'
data[81] = f'    error "Must be on a supported Heroku version: {", ".join(supportedHeroku)}"\n'
with open(scriptPath, 'w') as f:
    f.writelines(data)
