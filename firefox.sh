#!/bin/bash

# Function to check if Firefox needs an update
check_update() {
    current_version=$(firefox --version | awk '{print $3}')
    latest_version=$(curl -s https://www.mozilla.org/en-US/firefox/new/ | grep -oP 'Version \K[0-9.]+')

    if [[ $current_version == $latest_version ]]; then
        echo "Firefox is up to date."
    else
        echo "Firefox needs an update."
        perform_update
    fi
}

# Function to perform the update task
perform_update() {
    echo "Updating Firefox..."
    sudo apt update && sudo apt upgrade -y firefox
    echo "Firefox has been updated."
}

# Run the script every 2 weeks
while true; do
    check_update
    sleep 14d
done