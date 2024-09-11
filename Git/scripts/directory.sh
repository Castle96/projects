#!/bin/bash

# Define Variables
active_directory=$(pwd)

# Main script
echo "Active directory: $active_directory"
echo "Checking for existing domain controller..."

# Check if domain controller is already present
if [ -d "$active_directory" ]; then
    echo "Domain controller already exists in this directory."
else
    echo "No domain controller found in this directory."
fi

# Prompt user for domain controller name
read -p "Enter domain controller name: " dc_name


    # Check if domain controller name is valid
    if [ -z "$dc_name" ]; then
        echo "Domain controller name cannot be empty."
    else
        echo "Domain controller name: $dc_name"
    fi

    # Check if domain controller name already exists
    if [ -d "$dc_name" ]; then
        echo "Domain controller name already exists in this directory."
    else
        echo "Domain controller name does not exist in this directory."
    fi

    # Create domain controller directory
    mkdir -p "$dc_name"

    # Change directory to domain controller directory
    cd "$dc_name"

    # Create subdirectories
    mkdir -p "Users"
    mkdir -p "Groups"

    