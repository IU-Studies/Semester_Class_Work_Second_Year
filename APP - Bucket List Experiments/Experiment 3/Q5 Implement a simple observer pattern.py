""" Implement a simple observer pattern with a Subject class that manages a list of Observer objects.
Implement an Observer interface with an update method. Create concrete Observer classes
(EmailNotifier and SMSNotifier) that implement the update method. Demonstrate the observer
pattern by notifying observers of a change in the subject.
Concepts Covered: Observer Pattern """

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

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def change_state(self, state):
        self._state = state
        self.notify()

subject = Subject()

email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

subject.attach(email_notifier)
subject.attach(sms_notifier)

subject.change_state("State has changed to 'ACTIVE'")
