class ContextMemory:
    def __init__(self):
        self.sessions = {}

    def update(self, session_id, key, value):
        if session_id not in self.sessions:
            self.sessions[session_id] = {}
        self.sessions[session_id][key] = value

    def get(self, session_id, key):
        return self.sessions.get(session_id, {}).get(key, None)
