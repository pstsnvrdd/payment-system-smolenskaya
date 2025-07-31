from src.payment.observer import LoggingListener, AdminAlertListener
import logging

def test_logging_listener(caplog):
    listener = LoggingListener()
    with caplog.at_level(logging.INFO):
        listener.notify("payment_succeeded", {"lol": "kek"})
    assert "Event: payment_succeeded" in caplog.text

def test_admin_alert_listener(caplog):
    listener = AdminAlertListener()
    with caplog.at_level(logging.ERROR):
        listener.notify("payment_failed", {"lol": "kek"})
    assert "ALERT! Payment failed" in caplog.text