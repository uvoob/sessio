from .session import Session
from .exceptions import SessionNotFoundError
from .storage import Storage

class SessionService:
    def __init__(self, storage):
        if not isinstance(storage, Storage):
            raise TypeError("Storage must be an instance of Storage or its subclass")
        self.storage = storage
        
    def create_session(self, ttl=3600):
        session = Session()
        self.storage.save(session)
        return session.session_id
    
    def get_session(self, session_id):
        session = self.storage.load(session_id)
        if session and session.expire():
            self.storage.delete(session_id)
            raise SessionNotFoundError("Session has expired")
        return session
    
    def delete_session(self, session_id):
        self.storage.delete(session_id)