import logging

# Logging ko setup karna
def setup_logging():
    """
    Yeh function logging ko setup karta hai.
    args: None
    returns: setup_configration
    This function sets up the logging configuration for the application.
    """
    rsetup_configration = logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    return rsetup_configration


# level=logging.DEBUG This sets the log level to DEBUG.
# It means that all log messages of level DEBUG and above (like INFO, WARNING, ERROR, and CRITICAL) will be captured.
# format='%(asctime)s - %(levelname)s - %(message)s':
# This defines how the log messages will be formatted when they are printed or written to a file.
# %(asctime)s:
# This inserts the timestamp (date and time) when the log message is generated.
# Example: 2025-10-19 10:00:00,000
# %(levelname)s:
# This inserts the log level (like DEBUG, INFO, WARNING, etc.).
# Example: DEBUG
# %(message)s:
# This inserts the actual log message that you log using logger.debug(), logger.info(), etc.
# Example: This is a debug message
# Different levels ke log messages
# logging.debug('Yeh ek debug message hai')
# logging.info('Yeh ek info message hai')
# logging.warning('Yeh ek warning message hai')
# logging.error('Yeh ek error message hai')
# logging.critical('Yeh ek critical error hai')

def intro(name, age):
    if not name or not age:
        logging.error("Name ya age nahi di gayi hai.")
        return "Name ya age nahi di gayi hai."
    else:
        logging.info(f"Yeh name {name} hai aur ya mari age {age} hai.")
        return f"Hello, {name}! Aapki age {age} hai."
    


intro("John", 30 )
# Yeh code Python mein logging ka use karke alag-alag level ke messages ko print karta hai.
# logging module ko import karte hain.
# basicConfig se hum logging ka setup karte hain.
# level=logging.DEBUG se hum logging ka level define karte hain. Yani ki sabse zyada detail wale messages show hote hain.
# format se hum message ka format define karte hain.