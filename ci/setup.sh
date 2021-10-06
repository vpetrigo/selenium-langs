#!/bin/bash

set -euxo pipefail

curl "https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip" -o chromedriver_linux64.zip
unzip chromedriver_linux64.zip -d .
chmod +x ./chromedriver
./chromedriver --version
