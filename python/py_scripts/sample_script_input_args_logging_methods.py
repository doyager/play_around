from sys import argv
import time
import logging
import logging.handlers
import os
from datetime import datetime


## Usage :  
## To run : python test_pymain.py agent1 06232019 ui-portal 10


root = logging.getLogger()
root.setLevel(logging.DEBUG)

#handler = logging.StreamHandler(sys.stdout)
handler = logging.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", "/home/mac/test_area/script_agent_test/scripts/py_logs/pyscriptagnet_{:%Y-%m-%d_%H_%M_%S_%s}.log".format(datetime.now())))
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

def test_method() :
        logging.info("Inside test method")
        print("Hello World - Python Script Agent")
        print("Hello agent: "+AGENT_NAME+" for run-date: "+RUN_DATE)
        print("Sleeping for "+  SLEEP_DURATION + " seconds")
        print ("Sleep start : %s " % time.ctime())
        time.sleep(float(SLEEP_DURATION))
        print('Sleep end : %s\n' % time.ctime())
        logging.info("Exiting test method")


if __name__ == "__main__":
    logging.info("Inside main")
    print (">>>>Initializing the program..")
    print (">>>>Loading the arguments")
    #getOutliers()
    #exit(0)
    if len(argv) == 5:
        AGENT_NAME = argv[1]
        RUN_DATE = argv[2]
        SERVER_NAME = argv[3]
        SLEEP_DURATION = argv[4]
        test_method()
    else:
        print (">>>>Argument length error")
        exit(1)
