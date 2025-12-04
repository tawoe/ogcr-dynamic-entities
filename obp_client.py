import os
from dotenv import load_dotenv
import requests
from json import loads
import logging

load_dotenv()
obp_log_level = os.getenv('OBP_LOG_LEVEL', 'INFO')

logging.basicConfig(level=obp_log_level)
logger = logging.getLogger("obp")
logger.propagate = True


def create_direct_login_token(username, user_password, consumer_key, obp_api_host, verify=True):
	authorization = f"DirectLogin username={username},password={user_password},consumer_key={consumer_key}"
	headers = {'Content-Type': 'application/json', 'Authorization': authorization}

	payload = None
	url = obp_api_host + "/my/logins/direct"
	try:
		req = requests.post(url, headers=headers, json=payload, verify=verify)
		token = loads(req.text)["token"]
	except Exception as e:
		logger.exception(f'could not get direct login for: {url} user: {username}: {e}')
		token = None
	return token
obp_host = os.getenv('OBP_HOSTNAME', "http://obp-api-internal-route-obp.apps-crc.testing")
try:
	username = os.environ['OBP_USERNAME']
except KeyError:
	logger.exception('OBP_USERNAME not set in os environment or .env file! Exiting now.')
	exit(1)
try:
	password = os.environ['OBP_PASSWORD']
except KeyError:
	logger.exception('OBP_PASSWORD not set in os environment or .env file! Exiting now.')
	exit(1)
try:
	consumer_key = os.environ['OBP_CONSUMER_KEY']
except KeyError:
	logger.exception('OBP_CONSUMER_KEY not set in os environment or .env file! Exiting now.')
	exit(1)

token = create_direct_login_token(username, password, consumer_key, obp_host)



