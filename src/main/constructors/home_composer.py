from typing import Callable
from src.view.app_views.Windown import Windown
from src.view.app_views.HomeFrame import HomeFrame


def home_composer( master:Windown, start_command:Callable):

    home = HomeFrame(master=master, start_command=start_command,)

    return home