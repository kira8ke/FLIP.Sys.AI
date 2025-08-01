"""Configuration constants for the FLIP-sys.AI health checker script."""

FLIP_API_ENDPOINT = "https://api.flip-sys.ai/v1/incident-report"
TEST_PAYLOAD = {
    "incident_id": "test123",
    "timestamp": "2025-07-26T10:00:00Z",
    "vehicle_plate": "KDA123X",
    "location": "Nairobi, Kenya",
    "damage_severity": "minor",
    "images": ["https://dummyimage.com/test-damage.jpg"]
}

