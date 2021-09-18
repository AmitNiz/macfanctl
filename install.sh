#!/bin/env sh

echo -e "\n[*]Downloading..\n"
curl https://raw.githubusercontent.com/AmitNiz/macfanctl/main/macfanctl.py >  /tmp/macfanctl && \
echo -e "\n[*]Moving files to /usr/bin \n" && \
sudo chmod 755 /tmp/macfanctl && \
sudo mv /tmp/macfanctl /usr/bin

