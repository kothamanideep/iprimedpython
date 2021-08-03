import logging

logging.basicConfig(filename="demo.log",level=logging.DEBUG)


logging.critical("critical error happend")     #50

logging.error("an unknown error happend")     #40 
logging.warning("Expected value is an integer")    #30
logging.debug("for developers")             #10
logging.info("Normal message") #20