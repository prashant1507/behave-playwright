import requests
import json


def add_in_elk(context, logger, test_id, summary, status, author):
    response = None
    if context.details.getboolean("elk", "add_in_elk"):
        url = f"{context.details.get("elk", "elk_url")}/qa-test-case-logs/_doc?pipeline=add-timestamp-pipeline"
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
            
