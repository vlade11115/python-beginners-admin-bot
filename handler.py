import json
import os
from typing import Any, Dict

import aws_lambda_powertools
import requests
from aws_lambda_powertools.utilities.typing import LambdaContext

tracer = aws_lambda_powertools.Tracer(
    service="python-beginners-admin-bot", patch_modules=["boto3", "requests"]
)
logger = aws_lambda_powertools.Logger(
    service="python-beginners-admin-bot", level="INFO"
)


@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
def hello(event: Dict[str, Any], context: LambdaContext) -> Dict[str, Any]:
    token = os.getenv("token")
    for record in event["Records"]:
        body = json.loads(record["body"])
        logger.info(body)
        logger.info(requests.get(f"https://api.telegram.org/bot{token}/getMe").json())
    return event
