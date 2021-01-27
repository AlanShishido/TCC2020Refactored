import abc


class BaseViewController(abc.ABC):
    @abc.abstractmethod
    def show_view(self):
        pass

    @abc.abstractmethod
    def close_view(self):
        pass
