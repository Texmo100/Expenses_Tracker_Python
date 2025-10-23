from ui import *
from repositories import create_init_user, create_init_tracker

def app():
    user = create_init_user()
    tracker = create_init_tracker(user)
    main_menu()