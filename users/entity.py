from utils.entity import Entity


class UserEntity(Entity):
    username = str
    password = str
    email = str
    is_active = bool
    is_staff = bool
