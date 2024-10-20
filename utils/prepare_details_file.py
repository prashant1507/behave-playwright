import os
import json
from helpers.constants.framework_constants import FrameworkConstants as Fc


def prepare_details_file():
    file_path = Fc.details_file
    try:
        with open(file_path, "r") as file:
            config = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to load configuration from {file_path}: {e}")
    
    for key, value in os.environ.items():
        placeholder = f"${{{key}}}"
        if value.lower() == "true":
            config_str = config_str.replace(f'"{placeholder}"', 'true')
        elif value.lower() == "false":
            config_str = config_str.replace(f'"{placeholder}"', 'false')
        else:
            config_str = config_str.replace(placeholder, value)
    try:
        config = json.loads(config_str)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to parse updated configuration: {e}")
    try:
        with open(file_path, "w") as file:
            json.dump(config, file, indent=4)
    except IOError as e:
        raise RuntimeError(f"Failed to write configuration to {file_path}: {e}")

    config_str = json.dumps(config)
