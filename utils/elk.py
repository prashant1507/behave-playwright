import requests
import json
from helpers.constants.framework_constants import FrameworkConstants as Fc
from utils.helper_utils import read_file

url = "http://192.168.0.24:9200/qa-test-case-logs/_doc?pipeline=add-timestamp-pipeline"

def add_in_elk(logger, test_id, summary, status, author):
    details = read_file(Fc.details_file)

    if details["add_in_elk"]:
        data = {
            "test_id": test_id,
            "scenario": summary,
            "status": status,
            "author": author
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 201:
            logger.info(f"{test_id} {summary} {status} {author} | Document added successfully.")
        else:
            logger.info(f"Failed to add document. Status code: {response.status_code}")
            logger.info("Response:", response.json())
