class SimpleDatabase:
    def __init__(self):
        self.tables = {
            "users": {},
            "posts": {},
            "comments": {}
        }
        self.counters = {
            "users": 0,
            "posts": 0,
            "comments": 0
        }