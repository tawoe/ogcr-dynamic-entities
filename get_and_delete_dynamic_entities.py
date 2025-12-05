import requests
import logging
from obp_client import token, obp_host

# Configure logging
logger = logging.getLogger(__name__)

# Configuration
BASE_URL = obp_host  # Replace with your OBP instance URL
DIRECTLOGIN_TOKEN = token  # Optional: Replace with your DirectLogin token



def get_all_system_dynamic_entities(token=None):
	"""
	Get all system-level dynamic entities in OBP.

	Args:
		token (str, optional): DirectLogin authentication token

	Returns:
		dict: The API response
	"""
	url = f"{BASE_URL}/obp/v5.1.0/management/system-dynamic-entities"

	headers = {
		"Content-Type": "application/json"
	}

	# Add authentication if token is provided
	if token:
		headers["Authorization"] = f"DirectLogin token={token}"

	try:
		response = requests.get(url, headers=headers)
		response.raise_for_status()
		return response.json()
	except requests.exceptions.RequestException as e:
		logger.error(f"Error getting system dynamic entity: {e}")
		if hasattr(e.response, 'text'):
			logger.error(f"Response: {e.response.text}")
		raise

def get_all_objects_for_system_dynamic_entity(entity_name, token=None):
	"""
	Get all system-level dynamic entities in OBP.

	Args:
		token (str, optional): DirectLogin authentication token

	Returns:
		dict: The API response
	"""
	url = f"{BASE_URL}/obp/dynamic-entity/{entity_name}"

	headers = {
		"Content-Type": "application/json"
	}

	# Add authentication if token is provided
	if token:
		headers["Authorization"] = f"DirectLogin token={token}"

	try:
		response = requests.get(url, headers=headers)
		response.raise_for_status()
		return response.json()
	except requests.exceptions.RequestException as e:
		logger.error(f"Error getting system dynamic entity: {e}")
		if hasattr(e.response, 'text'):
			logger.error(f"Response: {e.response.text}")
		raise

def delete_object_for_system_dynamic_entity(entity_name, object_id, token=None):

	url = f"{BASE_URL}/obp/dynamic-entity/{entity_name}/{object_id}"

	headers = {
		"Content-Type": "application/json"
	}

	# Add authentication if token is provided
	if token:
		headers["Authorization"] = f"DirectLogin token={token}"

	try:
		response = requests.delete(url, headers=headers)
		response.raise_for_status()
		return response.json()
	except requests.exceptions.RequestException as e:
		logger.error(f"Error deleting system dynamic entity object: {e}")
		if hasattr(e.response, 'text'):
			logger.error(f"Response: {e.response.text}")
		raise

def delete_system_dynamic_entity(entity_id, token=None):

	url = f"{BASE_URL}/obp/v5.1.0/management/system-dynamic-entities/{entity_id}"

	headers = {
		"Content-Type": "application/json"
	}

	# Add authentication if token is provided
	if token:
		headers["Authorization"] = f"DirectLogin token={token}"

	try:
		response = requests.delete(url, headers=headers)
		response.raise_for_status()
		return response.json()
	except requests.exceptions.RequestException as e:
		logger.error(f"Error deleting system dynamic entity: {e}")
		if hasattr(e.response, 'text'):
			logger.error(f"Response: {e.response.text}")
		raise

