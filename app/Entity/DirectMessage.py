from app.Entity.Authentication import Authentication

class DirectMessage(Authentication):
    user_id: str
    message: str
