# Dynamic Entity Name Constants

This document describes the entity name constants used throughout the project.

## Overview

All dynamic entity names are defined as constants in `dynamic_entities.py` to ensure consistency across the codebase and make refactoring easier.

## Constants

The following constants are available:

```python
from dynamic_entities import (
    ENTITY_PROJECT,
    ENTITY_PARCEL,
    ENTITY_PARCEL_OWN_VERIFY,
    ENTITY_PROJ_PARCEL_VERIFY,
    ENTITY_PROJ_VERIFY,
    ENTITY_PARCEL_MON_PER_VERIFY,
    ENTITY_PROJ_PER_VERIFY
)
```

## Entity Names (with OGCR2 prefix)

| Constant | Value | Description |
|----------|-------|-------------|
| `ENTITY_PROJECT` | `OGCR2Project` | Carbon credit project |
| `ENTITY_PARCEL` | `OGCR2Parcel` | Land parcel |
| `ENTITY_PARCEL_OWN_VERIFY` | `OGCR2Parcel_Own_Verify` | Parcel ownership verification |
| `ENTITY_PROJ_PARCEL_VERIFY` | `OGCR2Proj_Parcel_Verify` | Project-parcel verification (baseline) |
| `ENTITY_PROJ_VERIFY` | `OGCR2Proj_Verify` | Project verification |
| `ENTITY_PARCEL_MON_PER_VERIFY` | `OGCR2Parcel_Mon_Per_Verify` | Parcel monitoring period verification |
| `ENTITY_PROJ_PER_VERIFY` | `OGCR2Proj_Per_Verify` | Project period verification |

**Note:** The prefix is configurable via the `OBP_ENTITY_PREFIX` environment variable in `.env`

## Character Count Compliance

All entity names are kept under 32 characters to comply with API limitations:

- ✓ OGCR2Project (12 chars)
- ✓ OGCR2Parcel (11 chars)
- ✓ OGCR2Parcel_Own_Verify (22 chars)
- ✓ OGCR2Proj_Parcel_Verify (23 chars)
- ✓ OGCR2Proj_Verify (16 chars)
- ✓ OGCR2Parcel_Mon_Per_Verify (26 chars)
- ✓ OGCR2Proj_Per_Verify (20 chars)

## Usage Examples

### In main.py

```python
from dynamic_entities import (
    ENTITY_PROJECT,
    ENTITY_PARCEL,
    # ... other constants
)

my_dynamic_entities_names = [
    ENTITY_PROJECT,
    ENTITY_PARCEL,
    ENTITY_PARCEL_OWN_VERIFY,
    ENTITY_PROJ_PARCEL_VERIFY,
    ENTITY_PROJ_VERIFY,
    ENTITY_PARCEL_MON_PER_VERIFY,
    ENTITY_PROJ_PER_VERIFY
]
```

### In create_dummy_data.py

```python
from dynamic_entities import ENTITY_PROJECT, ENTITY_PARCEL

# Create a project
response = create_dynamic_entity_object(
    ENTITY_PROJECT,
    {"project_owner": "John Smith"},
    token
)

# Create a parcel
response = create_dynamic_entity_object(
    ENTITY_PARCEL,
    {
        "project_id": project_id,
        "parcel_owner": "John Smith",
        "geo_data": '{"type":"Polygon",...}'
    },
    token
)
```

## Benefits

1. **Type Safety**: IDE autocomplete and type checking
2. **Refactoring**: Change entity names in one place
3. **Consistency**: No typos or inconsistent naming
4. **Documentation**: Clear definition of all entities
5. **Maintainability**: Easier to update if naming conventions change

## Relationships

### Entity Hierarchy

```
Project (ENTITY_PROJECT)
├── Parcel (ENTITY_PARCEL)
│   ├── Parcel Ownership Verification (ENTITY_PARCEL_OWN_VERIFY)
│   ├── Project-Parcel Verification (ENTITY_PROJ_PARCEL_VERIFY)
│   └── Parcel Monitoring Period Verification (ENTITY_PARCEL_MON_PER_VERIFY)
├── Project Verification (ENTITY_PROJ_VERIFY)
└── Project Period Verification (ENTITY_PROJ_PER_VERIFY)
```

### Foreign Key Relationships

- `ENTITY_PARCEL.project_id` → `ENTITY_PROJECT`
- `ENTITY_PARCEL_OWN_VERIFY.parcel_id` → `ENTITY_PARCEL`
- `ENTITY_PROJ_PARCEL_VERIFY.parcel_id` → `ENTITY_PARCEL`
- `ENTITY_PROJ_PARCEL_VERIFY.project_id` → `ENTITY_PROJECT`
- `ENTITY_PROJ_VERIFY.project_id` → `ENTITY_PROJECT`
- `ENTITY_PARCEL_MON_PER_VERIFY.parcel_id` → `ENTITY_PARCEL`
- `ENTITY_PARCEL_MON_PER_VERIFY.project_id` → `ENTITY_PROJECT`
- `ENTITY_PROJ_PER_VERIFY.project_id` → `ENTITY_PROJECT`
