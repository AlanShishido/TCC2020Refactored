from src import models
from src.view_router import ViewRouter
from src.views.base_view_controller import BaseViewController
from src.views.main_view_model import MainViewModel
from src.views.main_view import MainView


class MainViewController(BaseViewController):
    def __init__(self, view_router: ViewRouter):
        super(MainViewController, self).__init__()
        # instance attributes
        self.view_router: ViewRouter = view_router
        # initializing view and model instances
        self.view: MainView = MainView(
            close_click_callback=self.on_close_click_callback
        )
        self.model: MainViewModel = MainViewModel()
        # loading all data
        self._load_nutrients_data()
        self._load_customers_data()

    def on_close_click_callback(self):
        self.close_view()

    def _load_nutrients_data(self):
        self.model.nutrients.clear()
        self.model.nutrients.extend(models.Nutrient.select())
        self.view.update_nutrients_data(nutrients=self.model.nutrients)

    def _load_customers_data(self):
        self.model.customers.clear()
        self.model.customers.extend(models.Customer.select())
        self.view.update_customers_data(customers=self.model.customers)

    def show_view(self):
        super(MainViewController, self).show_view()
        self.view.show()

    def close_view(self):
        super(MainViewController, self).close_view()
        self.view.close()
