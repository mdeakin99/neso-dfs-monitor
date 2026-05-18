"""Constants for NESO DFS Monitor."""

DOMAIN = "neso_dfs_monitor"

# NESO API
NESO_API_URL = "https://api.neso.energy/api/3/action/datastore_search_sql"
NESO_RESOURCE_ID = "cc36fff5-5f6f-4fde-8932-c935d982ecd8"

# Config entry keys
CONF_NOTIFY_SERVICE = "notify_service"
CONF_NOTIFY_ON_ACCEPTED = "notify_on_accepted"
CONF_SCAN_INTERVAL = "scan_interval"

# Defaults
DEFAULT_SCAN_INTERVAL = 30  # minutes
DEFAULT_NOTIFY_ON_ACCEPTED = True

# Date fields to check in NESO response (tried in order)
DATE_FIELDS = [
    "SERVICE_DATE",
    "DELIVERY_DATE",
    "REQUIREMENT_DATE",
    "SP_START_DATE_TIME",
]

# Sensor
SENSOR_NAME = "NESO DFS Bid Status"
SENSOR_UNIQUE_ID = "neso_dfs_bid_status"

# States
STATE_ACCEPTED = "accepted"
STATE_NONE = "none"
STATE_ERROR = "error"
