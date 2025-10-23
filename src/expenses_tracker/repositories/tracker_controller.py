from models import *

def create_init_user():
    user = User('isaac', 'iniguez', '6621194658', 'luna olivarria 245')
    return user

def create_init_tracker(user):
    tracker = Tracker(user)
    return tracker
