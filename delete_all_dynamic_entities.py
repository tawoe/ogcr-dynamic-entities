import logging
from get_and_delete_dynamic_entities import (
    get_all_system_dynamic_entities,
    get_all_objects_for_system_dynamic_entity,
    delete_object_for_system_dynamic_entity,
    delete_system_dynamic_entity
)
from obp_client import token, obp_host

# Configure logging with better formatting
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Configuration
BASE_URL = obp_host
DIRECTLOGIN_TOKEN = token


def print_separator(char="=", length=80):
    """Print a separator line for better visual separation"""
    logger.info(char * length)


def main():
    logger.info("Starting Delete ALL Dynamic Entities Script")
    logger.warning("⚠️  WARNING: This will delete ALL system dynamic entities!")
    print_separator()
    
    # =========================================================================
    # STEP 1: Get all dynamic entities
    # =========================================================================
    logger.info("STEP 1: Retrieving all dynamic entities")
    print_separator("-")
    
    try:
        response = get_all_system_dynamic_entities(token=DIRECTLOGIN_TOKEN)
        all_dynamic_entities = response["dynamic_entities"]
        logger.info(f"✓ Found {len(all_dynamic_entities)} total dynamic entities")
    except Exception as e:
        logger.error(f"✗ Failed to retrieve dynamic entities: {e}")
        return
    
    if not all_dynamic_entities:
        logger.info("No dynamic entities found. Nothing to delete.")
        print_separator()
        return
    
    # Log all entity names
    logger.info("Dynamic entities to be deleted:")
    for idx, entity in enumerate(all_dynamic_entities, 1):
        entity_name = list(entity.keys())[1]  # Second key is the entity name
        entity_id = entity.get("dynamicEntityId", "N/A")
        logger.info(f"  [{idx}] {entity_name} (ID: {entity_id})")
    
    print_separator()
    
    # =========================================================================
    # STEP 2: Delete all entity objects for each dynamic entity
    # =========================================================================
    logger.info("STEP 2: Deleting all entity objects")
    print_separator("-")
    
    total_objects_deleted = 0
    total_objects_failed = 0
    
    for idx, entity in enumerate(all_dynamic_entities, 1):
        entity_name = list(entity.keys())[1]  # Second key is the entity name
        logger.info(f"[{idx}/{len(all_dynamic_entities)}] Processing entity: {entity_name}")
        
        try:
            response = get_all_objects_for_system_dynamic_entity(entity_name, token=DIRECTLOGIN_TOKEN)
            # Handle case where the list key might not exist (no objects)
            objects = response.get(f"{entity_name.lower()}_list", [])
            
            if not objects:
                logger.info(f"  → No objects found for {entity_name}")
                continue
            
            logger.info(f"  ✓ Found {len(objects)} object(s) for {entity_name}")
            
        except Exception as e:
            # This is an actual error (API failure, auth issue, etc.)
            logger.error(f"  ✗ API error while fetching objects for {entity_name}: {e}")
            continue
        
        object_ids = [x[f'{entity_name.lower()}_id'] for x in objects]
        logger.info(f"  → Object IDs: {', '.join(object_ids[:5])}{' ...' if len(object_ids) > 5 else ''}")
        
        for obj_idx, obj_id in enumerate(object_ids, 1):
            try:
                delete_object_for_system_dynamic_entity(entity_name, obj_id, token=DIRECTLOGIN_TOKEN)
                logger.info(f"  ✓ [{obj_idx}/{len(object_ids)}] Deleted object: {obj_id}")
                total_objects_deleted += 1
            except Exception as e:
                logger.error(f"  ✗ [{obj_idx}/{len(object_ids)}] Failed to delete object {obj_id}: {e}")
                total_objects_failed += 1
        
        logger.info("")  # Empty line for readability
    
    print_separator("-")
    logger.info(f"Object Deletion Summary: {total_objects_deleted} deleted, {total_objects_failed} failed")
    print_separator()
    
    # =========================================================================
    # STEP 3: Delete all dynamic entity definitions
    # =========================================================================
    logger.info("STEP 3: Deleting all dynamic entity definitions")
    print_separator("-")
    
    total_entities_deleted = 0
    total_entities_failed = 0
    
    for idx, entity in enumerate(all_dynamic_entities, 1):
        entity_name = list(entity.keys())[1]  # Second key is the entity name
        entity_id = entity["dynamicEntityId"]
        
        try:
            delete_system_dynamic_entity(entity_id, token=DIRECTLOGIN_TOKEN)
            logger.info(f"  ✓ [{idx}/{len(all_dynamic_entities)}] Deleted entity: {entity_name} (ID: {entity_id})")
            total_entities_deleted += 1
        except Exception as e:
            logger.error(f"  ✗ [{idx}/{len(all_dynamic_entities)}] Failed to delete entity {entity_name}: {e}")
            total_entities_failed += 1
    
    print_separator("-")
    logger.info(f"Entity Deletion Summary: {total_entities_deleted} deleted, {total_entities_failed} failed")
    print_separator()
    
    logger.info("Delete ALL Dynamic Entities Script Completed")
    print_separator("=")


if __name__ == "__main__":
    main()