import logging 
  
# Create and configure logger 
logging.basicConfig(filename="newfile.log", 
                    format='%(levelname)s %(asctime)s %(message)s', 
                    filemode='w') 
logger = logging.getLogger()  
logger.setLevel(logging.DEBUG) 
