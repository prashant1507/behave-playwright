import requests
import json
from helpers.constants.framework_constants import FrameworkConstants as Fc
from utils.helper_utils import read_file


def add_in_elk(logger, test_id, summary, status, author):
    details = read_file(Fc.details_file)

    if details["elk"]["add_in_elk"]:
        url = f"{details["elk"]["elk_url"]}/qa-test-case-logs/_doc?pipeline=add-timestamp-pipeline"
        data = {
            "test_id": str(test_id),
            "scenario": summary,
            "status": status,
            "author": author
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            response.raise_for_status()
        except Exception as e:
            logger.info(f"Failed to add document. Status code: {response.status_code}")
            logger.info("Response:", response.json())
            
