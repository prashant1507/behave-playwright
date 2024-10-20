import os
import re
from helpers.constants.framework_constants import FrameworkConstants


def prepare_details_file() -> None:
    file_path = FrameworkConstants.details_file
    pattern = re.compile(r'"\$\{(\w+)}"|\$\{(\w+)}')

    with open(file_path, "r") as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        new_line = pattern.sub(
            lambda m: os.environ.get(m.group(1) or m.group(2), m.group(0)),
            line
        )
        new_lines.append(new_line)

    with open(file_path, "w") as file:
        file.writelines(new_lines)