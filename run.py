from src.main.process_handler import ProcessHandler

from src.view.app_views.Windown import Windown
from src.view.app_views.TelaLogin import Telalogin
from src.view.app_views.AdminFrame import AdminFrame
from src.view.app_views.CadAlunoFrame import CadAlunoFrame
from src.view.app_views.RankingFrame import RankingFrame
from src.view.app_views.AddQuestFrame import AddQuestFrame
if __name__ == "__main__":

    j = Windown()
    t = AddQuestFrame(master=j)
    t.place(x = 0, y = 0)
    j.mainloop()
