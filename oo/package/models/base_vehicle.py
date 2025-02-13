from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_model(self):
        pass
