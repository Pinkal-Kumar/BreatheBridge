import uuid
from datetime import datetime

def initialize_state():
    return {
        "user_name": "", 
        "session_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "conversation": []
    }
