from loguru import logger

def log(response, request_body=None):
    logger.info(f"REQUEST METOD: {response.request.method}")
    logger.info(f"REQUEST URL: {response.url}")
    logger.info(f"REQUEST HEADERS: {response.request.headers}")
    logger.info(f"REQUEST BODY: {request_body}")
    logger.info(f"STATUS CODE: {response.status_code}")
    logger.info(f"RESPONSE TIME: {response.elapsed.total_seconds() * 1000:.0f} ms")
    logger.info(f"RESPONSE HEADERS: {response.headers}")
    logger.info(f"RESPONSE BODY: {response.text}")