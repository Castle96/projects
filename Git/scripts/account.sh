#!/bin/bash
THRESHOLD=80
USAGE=$(df -h / | awk 'NR==2{print $5}' | sed 's/%//g')

if [ $USAGE -gt $THRESHOLD ]; then
    echo "Disk usage threshold exceeded: $USAGE%"
    exit 1
fi