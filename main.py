import requests
from obp_client import token, obp_host


from get_and_delete_dynamic_entities import (
	get_all_system_dynamic_entities,
	get_all_objects_for_system_dynamic_entity,
	delete_object_for_system_dynamic_entity,
	delete_system_dynamic_entity)
from dynamic_entities import create_all_entities, PREFIX

# Configuration
BASE_URL = obp_host
DIRECTLOGIN_TOKEN = token

my_dynamic_entities_names =[
	f"{PREFIX}Project",
	f"{PREFIX}Parcel",
	f"{PREFIX}Parcel_Ownership_Verification",
	f"{PREFIX}Project_Parcel_Verification",
	f"{PREFIX}Project_Verification",
	f"{PREFIX}Parcel_Monitoring_Period_Verification",
	f"{PREFIX}Project_Period_Verification"
]


# Delete all entity objects for each dynamic entity listed above
for name in my_dynamic_entities_names:
	try:
		objects = get_all_objects_for_system_dynamic_entity(name, token=DIRECTLOGIN_TOKEN)[f"{name.lower()}_list"]
	except Exception as e:
		print(f'could not get objects for entity {name}: {e}')
		continue
	object_ids = [x[f'{name.lower()}_id'] for x in objects]
	print(f'this are the object ids: {object_ids}')
	for id in object_ids:
		try:
			delete_object_for_system_dynamic_entity(name, id, token=DIRECTLOGIN_TOKEN)
		except Exception as e:
			print(f'could not delete object id {id} for entity {name}: {e}')


# Delete the dynamic entities themselves
all_dynamic_entities = (get_all_system_dynamic_entities(token=DIRECTLOGIN_TOKEN))["dynamic_entities"]
my_dynamic_entities = [x for x in all_dynamic_entities if list(x.keys())[1] in my_dynamic_entities_names]
my_dynamic_entities_ids = [x["dynamicEntityId"] for x in my_dynamic_entities]
for id in my_dynamic_entities_ids:
	try:
		delete_system_dynamic_entity(id, token=DIRECTLOGIN_TOKEN)
	except Exception as e:
		print(f'could not delete system dynamic entity {id}: {e}')


# (Re)create all dynamic entities.
create_all_entities()