import uuid

def generate_unique_id():
    """Generates a unique identifier for models."""
    return uuid.uuid4().hex[:8]