#!/bin/sh
SCRIPT=$(readlink -f $0)
SCRIPTPATH=$(dirname $SCRIPT)
if [ $# -eq 0 ]; then 
    echo "Usage: install.sh <install | purge | link>"
else
    if [ -w /usr/bin ] || [ "$1" = "link" ]; then
        if [ "$1" = "install" ]; then
            if cp ${SCRIPTPATH}/pebblesay.py /usr/bin/pebblesay && chmod +x /usr/bin/pebblesay; then
                echo "Installed successfully."
            fi
        elif [ "$1" = "purge" ]; then
            if rm /usr/bin/pebblesay; then
                echo "Uninstalled successfully."
            fi
        elif [ "$1" = "link" ]; then
            chmod +x pebblesay.py
            ln pebblesay.py pebblesay
            printf "\n# adding the folder containing pebblesay to the \$PATH variable.\n" >> ~/.bashrc
            printf "export PATH=\$PATH\":$SCRIPTPATH\"" >> ~/.bashrc
            echo "Please reopen your terminal window."
        else
            echo "Error: Wrong argument."
        fi
    else
        if command -v sudo > /dev/null; then
            sudo sh $SCRIPT $1
        else
            su -c "sh $SCRIPT $1"
        fi
    fi
fi
