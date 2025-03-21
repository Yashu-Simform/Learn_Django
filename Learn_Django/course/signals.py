from django.dispatch import Signal


notify = Signal()

def notifyAll(sender, *args, **kwargs):
    pass