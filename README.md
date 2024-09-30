# Plutus
    Stock data analysis from tushare

## Package server with pyinstaller
    pyinstaller -F server.py --add-data="./config.json;." --add-data="./logging.conf;."

## docker build server image
    sudo docker build -t plutus/server:latest .

