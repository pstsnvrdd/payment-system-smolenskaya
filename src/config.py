from dotenv import load_dotenv
import os

load_dotenv()  #loads variables from a file .env in the environment

class Config:
    payment_provider = os.getenv("PAYMENT_PROVIDER", "stripe")   #payment system settings
    tax_rate = float(os.getenv("TAX_RATE", 0.07))                #tax (default = 7%)
    discount_rate = float(os.getenv("DISCOUNT_RATE", 0.0))       #discount (default = 0)