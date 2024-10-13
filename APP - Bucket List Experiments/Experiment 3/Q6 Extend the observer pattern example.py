""" Extend the observer pattern example to include a method add_observer in the Subject class to add
observers. Implement a method notify_observers that calls update on each observer. Demonstrate
adding and notifying multiple observers.
Concepts Covered: Observer Pattern with Observer Management """ 

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class EmailNotifier(Observer):
    def update(self, message):
        print(f"Email Notifier: {message}")

class SMSNotifier(Observer):
    def update(self, message):
        print(f"SMS Notifier: {message}")

class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._state)

    def change_state(self, state):
        self._state = state
        self.notify_observers()

subject = Subject()

email_notifier1 = EmailNotifier()
email_notifier2 = EmailNotifier()  
sms_notifier = SMSNotifier()

subject.add_observer(email_notifier1)
subject.add_observer(email_notifier2)
subject.add_observer(sms_notifier)

subject.change_state("State has changed to 'ACTIVE'")
