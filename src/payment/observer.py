from src.payment.interfaces import PaymentEventListener
import logging

class LoggingListener(PaymentEventListener):
    def notify(self, event: str, data: dict):
        logging.info(f"Event: {event}, Data: {data}")

class AdminAlertListener(PaymentEventListener):
    def notify(self, event: str, data: dict):
        if event == "payment_failed":
            logging.error(f"ALERT! Payment failed: {data}")