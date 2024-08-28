#!/bin/bash

# Define Variables
CURRENT_VERSION_FILE="$HOME/.config/obsidian/version.txt"
LATEST_VERSION_URL="https://api.github.com/repos/obsidianmd/obsidian-releases/releases/latest"
DOWNLOAD_BASE_URL="https://github.com/obsidianmd/obsidian-releases/releases/download"
INSTALL_PATH="/usr/local/bin"

# Function to get the current version
get_current_version() {
    if [ -f "$CURRENT_VERSION_FILE" ]; then
        cat "$CURRENT_VERSION_FILE"
    else
        echo "0.0.0"
    fi
}

# Function to get the latest version
get_latest_version() {
    curl -s "$LATEST_VERSION_URL" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/'
}

# Function to download the latest version
download_latest_version() {
    local latest_version="$1"
    local download_url="$DOWNLOAD_BASE_URL/$latest_version/obsidian_${latest_version}_amd64.deb"

    echo "Downloading Obsidian latest version..."
    curl -L -o obsidian.AppImage "$download_url"

    # Make the downloaded file executable
    chmod +x "$INSTALL_PATH/obsidian.AppImage"

    echo "Obsidian latest version downloaded successfully."
    echo "Current version: $latest_version"
}

# Main script
current_version=$(get_current_version)
latest_version=$(get_latest_version)

if [ "$current_version" != "$latest_version" ]; then
    download_latest_version "$latest_version"
fi