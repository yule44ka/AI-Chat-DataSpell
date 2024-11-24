#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Install required packages
echo "Installing required packages..."
pip install -r requirements.txt

# Check if .env file exists and prompt user to create one if not
if [[ ! -f ".env" ]]; then
    echo "No .env file found. Creating one..."
    touch .env
    echo "Please enter your OpenAI API Key:"
    read -r OPENAI_API_KEY
    echo "OPENAI_API_KEY=$OPENAI_API_KEY" > .env
    echo ".env file created with the provided API key."
else
    echo ".env file found. Skipping creation."
fi