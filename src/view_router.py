from typing import Type

from src.views.base_view_controller import BaseViewController


class ViewRouter(object):
    def __init__(self):
        self.router_dict: dict = {}
        self.current_view_controller: BaseViewController = None

    def add_route(self, view_name: str, view_controller: Type[BaseViewController]):
        self.router_dict[view_name] = view_controller

    def go_to_view(self, view_name: str):
        if view_name not in self.router_dict:
            return

        if self.current_view_controller:
            self.current_view_controller.close_view()
        self.current_view_controller = self.router_dict[view_name](view_router=self)
        self.current_view_controller.show_view()
