import uuid
import time

class Session:
    def __init__(self, session_id=None, ttl=3600):
        self.session_id = session_id or str(uuid.uuid4())
        self.created_at = time.time()
        self.data = {}
        self.ttl = ttl
        
    def set(self, key, value):
        self.data[key] = value
        
    def get(self, key):
        return self.data.get(key)
    
    def expire(self):
        return time.time() - self.created_at > self.ttl