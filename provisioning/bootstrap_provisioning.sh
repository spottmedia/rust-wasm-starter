#!/bin/bash

sudo apt install virtualenv build-essential nginx

virtualenv provisioningenv
. provisioningenv/bin/activate
pip install -r provisioning-requirements.txt
