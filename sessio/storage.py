import os
import pickle
from .session import Session

class Storage:
    """Storage api"""
    def save():
        raise NotImplementedError
    
    def load():
        raise NotImplementedError
    
    def delete():
        raise NotImplementedError

class MemoryStorage(Storage):
    """Storing sessions in memory"""
    def __init__(self):
        self.sessions = {}
        
    def save(self, session):
        self.sessions[session.session_id] = session
        
    def load(self, session_id):
        return self.sessions.get(session_id)
        
    def delete(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]

class FileStorage(Storage):
    """Storing sessions in file"""
    def __init__(self, storage_dir="sessions"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)
    
    def _session_file_path(self, session_id):
        return os.path.join(self.storage_dir, f"{session_id}.sessio")
        
    def save(self, session):
        path = self._session_file_path(session.session_id)
        with open(path, "wb") as f:
            pickle.dump(session, f)
        
    def load(self, session_id):
        path = self._session_file_path(session_id)
        if os.path.exists(path):
            with open(path, "rb") as f:
                session = pickle.load(f)
                if not session.expire():
                    return session
        return None
    
    def delete(self, session_id):
        path = self._session_file_path(session_id)
        if os.path.exists(path):
            os.remove(path)