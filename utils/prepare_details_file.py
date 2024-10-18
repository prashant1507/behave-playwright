import os
import json
from helpers.constants.framework_constants import FrameworkConstants as Fc


def prepare_details_file():
    file_path = Fc.details_file
    with open(file_path, "r") as file:
        config = json.load(file)
    config_str = json.dumps(config)

    for key, value in os.environ.items():
        placeholder = f"${{{key}}}"
        if value.lower() == "true":
            config_str = config_str.replace(f'"{placeholder}"', 'true')
        elif value.lower() == "false":
            config_str = config_str.replace(f'"{placeholder}"', 'false')
        else:
            config_str = config_str.replace(placeholder, value)

    config = json.loads(config_str)

    with open(file_path, "w") as file:
        json.dump(config, file, indent=4)

