# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:59:46 2024

@author: raxephion

Keyboard key remapper


Requirements:

bash
pip install keyboard

"""

import keyboard
import json

# Default key mappings - can be customized by the user
key_mapping = {
    'a': 'b',  # Replace 'a' with 'b'
    'b': 'c',  # Replace 'b' with 'c'
    'c': 'a',  # Replace 'c' with 'a'
}

# Function to load key mappings from a JSON file
def load_mappings_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Function to save key mappings to a JSON file
def save_mappings_to_file(filename, mappings):
    with open(filename, 'w') as file:
        json.dump(mappings, file, indent=4)

# Function to remap keys based on the key_mapping dictionary
def remap_keys(key_mapping):
    for src_key, dest_key in key_mapping.items():
        # Unhook any previously registered hotkeys to avoid conflicts
        keyboard.unhook_all_hotkeys()
        
        # Register a hotkey for the source key to be replaced by the destination key
        keyboard.add_hotkey(src_key, lambda dest_key=dest_key: keyboard.write(dest_key), suppress=True)

# Main function to run the key remapper
def main():
    global key_mapping
    key_mapping_filename = 'key_mappings.json'
    
    # Load key mappings from file
    key_mapping = load_mappings_from_file(key_mapping_filename)
    
    while True:
        print('Current key mappings:', key_mapping)
        user_input = input("Enter mappings in the format 'key:replacement' (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        try:
            key, replacement = user_input.split(':')
            key_mapping[key] = replacement
            # Save updated mappings to file
            save_mappings_to_file(key_mapping_filename, key_mapping)
        except ValueError:
            print("Invalid format. Please enter mappings in 'key:replacement' format.")
    
    print("Starting key remapper...")
    remap_keys(key_mapping)
    
    # Keep the script running to listen for key events
    print("Key remapper is active. Press 'esc' to stop.")
    keyboard.wait('esc')

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
