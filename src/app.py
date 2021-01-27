from src import consts
from src.view_router import ViewRouter
from src.views.main_view_controller import MainViewController


class App(object):
    def __init__(self):
        self._view_router: ViewRouter = self._init_view_router()

    @staticmethod
    def _init_view_router() -> ViewRouter:
        view_router: ViewRouter = ViewRouter()
        view_router.add_route(view_name=consts.vn_main_view, view_controller=MainViewController)
        return view_router

    def run(self):
        # show main view when application starts
        self._view_router.go_to_view(view_name=consts.vn_main_view)
