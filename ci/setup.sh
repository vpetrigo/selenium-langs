#!/bin/bash

set -euxo pipefail

curl "https://chromedriver.storage.googleapis.com/76.0.3809.68/chromedriver_linux64.zip" -o chromedriver_linux64.zip
unzip chromedriver_linux64.zip
export PATH=`pwd`:$PATH
