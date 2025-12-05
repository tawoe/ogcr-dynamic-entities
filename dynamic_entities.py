import requests
import logging
import json
from obp_client import token, obp_host
from dotenv import load_dotenv
import os

# Configure logging
logger = logging.getLogger(__name__)
# Configuration
BASE_URL = obp_host  # Replace with your OBP instance URL
DIRECTLOGIN_TOKEN = token  # Optional: Replace with your DirectLogin token
load_dotenv()
PREFIX = os.getenv('OBP_ENTITY_PREFIX', '')

def create_system_dynamic_entity(entity_definition, token=None):
	"""
	Create a system-level dynamic entity in OBP.

	Args:
		entity_definition (dict): The dynamic entity definition
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
		response = requests.post(url, headers=headers, json=entity_definition)
		response.raise_for_status()
		return response.json()
	except requests.exceptions.RequestException as e:
		logger.error(f"Error creating system dynamic entity: {e}")
		logger.error(f"Request URL: {url}")
		logger.error(f"Request body:\n{json.dumps(entity_definition, indent=2)}")
		if hasattr(e.response, 'text'):
			logger.error(f"Response: {e.response.text}")
		raise


# Example 1: Customer Preferences Entity
project_entity = {
	"hasPersonalEntity": False,  # Creates both regular and 'my' endpoints
	f"{PREFIX}Project": {
		"description": "a carbon credit project",
		"required": [
			"project_owner"
		],
		"properties": {
			"project_owner": {
				"type": "string",
				"example": "hugo muller passport nr. 1234444",
				"description": "legal identifier of landholder"
			}
		}
	},
}

parcel_entity = {
	"hasPersonalEntity": False,  # Creates both regular and 'my' endpoints
	f"{PREFIX}Parcel": {
				"description": "a piece of land",
				"required": [
					"project_id",
					"parcel_owner",
					"geo_data"
				],
				"properties": {
					"project_id": {
						"type": "string",
						"example": "1234567",
						"description": "ID of the project this parcel belongs to"
					},
					"parcel_owner": {
						"type": "string",
						"example": "hugo muller passport nr. 1234444",
						"description": "legal identifier of landholder"
					},
					"geo_data": {
						"type": "string",
						"example": "some_geo_json",
						"description": "a geojson polygon"
					}
				}
	}
}

parcel_ownership_verification_entity = {
	"hasPersonalEntity": False,
	f"{PREFIX}Parcel_Own_Verify": {
				"description": "Verification of Landownership",
				"required": [
					"parcel_id"
				],
				"properties": {
					"parcel_id": {
						"type": "string",
						"example": "3dece208-c95c-11f0-9041-54e1adfac5b1",
						"description": "(uu)id of the parcel that gets verified"
					},
					"status_code": {
						"type": "string",
						"example": "verified",
						"description": "in_progress, verified, failed"
					},
					"status_message": {
						"type": "string",
						"example": "could not find owner",
						"description": "further explanation of status code"
					},
					"authority": {
						"type": "string",
						"example": "Mycountry cadastre",
						"description": "name of  authority that verified the ownership"
					}
				}
	}
}

parcel_verification_entity = {
	"hasPersonalEntity": False,  # Creates both regular and 'my' endpoints
	f"{PREFIX}Proj_Parcel_Verify": {
		"description": "Verification of Project Claim Estimation",
		"required": [
			"parcel_id",
			"project_id"
		],
		"properties": {
			"parcel_id": {
				"type": "string",
				"example": "3dece208-c95c-11f0-9041-54e1adfac5b1",
				"description": "(uu)id of the parcel that gets verified"
			},
			"project_id": {
						"type": "string",
						"example": "3dece208-c95c-11f0-9041-54e1adfac5b1",
						"description": "ID of the project this parcel belongs to"
			},
			"status_code": {
				"type": "string",
				"example": "verified",
				"description": "in_progress, verified, failed"
			},
			"status_message": {
				"type": "string",
				"example": "x behaved badly",
				"description": "further explanation of status code"
			},
			"amount": {
				"type": "integer",
				"example": 6,
				"description": "amount of carbon reduction calculated"
			}
		}
	}}

project_verification_entity = {
	"hasPersonalEntity": False,  # Creates both regular and 'my' endpoints
	f"{PREFIX}Proj_Verify": {
		"description": "Verification of Project",
		"required": [
			"project_id"
		],
		"properties": {
			"project_id": {
						"type": "string",
						"example": "3dece208-c95c-11f0-9041-54e1adfac5b1",
						"description": "ID of the project verified"
			},
			"status_code": {
				"type": "string",
				"example": "verified",
				"description": "in_progress, verified, failed"
			},
			"status_message": {
				"type": "string",
				"example": "x behaved badly",
				"description": "further explanation of status code"
			}
		}
	}}

parcel_monitoring_period_verification = {
	"hasPersonalEntity": False,  # Creates both regular and 'my' endpoints
	f"{PREFIX}Parcel_Mon_Per_Verify": {
		"description": "Verification of Project Claim",
		"required": [
			"parcel_id",
			"project_id"
		],
		"properties": {
			"parcel_id": {
				"type": "string",
				"example": "3dece208-c95c-11f0-9041-54e1adfac5b1",
				"description": "(uu)id of the parcel that gets verified"
			},
			"project_id": {
						"type": "string",
						"example": "3dece208-c95c-11f0-9041-54e1adfac5b1",
						"description": "ID of the project this parcel belongs to"
			},
			"status_code": {
				"type": "string",
				"example": "verified",
				"description": "in_progress, verified, failed"
			},
			"status_message": {
				"type": "string",
				"example": "x behaved badly",
				"description": "further explanation of status code"
			},
			"amount": {
				"type": "integer",
				"example": 6,
				"description": "amount of carbon reduction calculated"
			}
		}
	}}

project_monitoring_period_verification = {
	"hasPersonalEntity": False,  # Creates both regular and 'my' endpoints
	f"{PREFIX}Proj_Per_Verify": {
		"description": "Verification of Project",
		"required": [
			"project_id"
		],
		"properties": {
			"project_id": {
						"type": "string",
						"example": "3dece208-c95c-11f0-9041-54e1adfac5b1",
						"description": "ID of the project verified"
			},
			"status_code": {
				"type": "string",
				"example": "verified",
				"description": "in_progress, verified, failed"
			},
			"status_message": {
				"type": "string",
				"example": "x behaved badly",
				"description": "further explanation of status code"
			}
		}
	}}


def create_all_entities():
	entities_data = [
		("Project", project_entity),
		("Parcel", parcel_entity),
		("Parcel_Own_Verify", parcel_ownership_verification_entity),
		("Proj_Parcel_Verify", parcel_verification_entity),
		("Proj_Verify", project_verification_entity),
		("Parcel_Mon_Per_Verify", parcel_monitoring_period_verification),
		("Proj_Per_Verify", project_monitoring_period_verification)
	]
	
	created_count = 0
	failed_count = 0
	
	for idx, (name, entity) in enumerate(entities_data, 1):
		full_name = f"{PREFIX}{name}"
		try:
			response = create_system_dynamic_entity(entity, DIRECTLOGIN_TOKEN)
			entity_id = response.get('dynamicEntityId', 'N/A')
			logger.info(f"  ✓ [{idx}/{len(entities_data)}] Created entity: {full_name} (ID: {entity_id})")
			created_count += 1
		except Exception as e:
			logger.error(f"  ✗ [{idx}/{len(entities_data)}] Failed to create entity {full_name}")
			logger.error(f"      Error details: {e}")
			# The detailed request is already logged by create_system_dynamic_entity()
			failed_count += 1
	
	logger.info("")
	logger.info(f"Entity Creation Summary: {created_count} created, {failed_count} failed")
