import os
import shutil
from sys import argv
import time
import warnings

#env dir setup
def env_dir_check():
    preprocess_dir='/tmp/preprocess'
    if not os.path.exists(preprocess_dir):
        os.makedirs(preprocess_dir)

#env dir clean up       
def env_dir_cleanup():
    if os.path.exists(preprocess_dir):
        shutil.rmtree(preprocess_dir)
        
#method to add our python files dir to the python run time        
def env_setup():
        code_dir = os.path.expanduser(project_dir)

        if code_dir not in sys.path:
                sys.path.append(code_dir)
        warnings.filterwarnings("ignore")

#main process
def process():
    
    try:
    
    #do something
    start_time = time.time()
    
    
    #after process
    print("\n Process finished in %s minutes \n" % ((time.time() - start_time) / 60))
    
    #cleanup    
    env_dir_cleanup()
    exit(0)
    
    
    except Exception as e:
            print ("[ERROR]  Process Failed  ")
            print ("ERROR : ")
            print (e)
            env_dir_cleanup()
            exit(1)
            
            
            
if __name__ == "__main__":
    if len(argv) == 3 :
        print (">>>>Args Passed: Loading the arguments")
        project_dir = argv[1]
        tmp_dir = argv[2]
        threshold = argv[3]
        print (">>>>Args Received: "+"\n project_dir: "+project_dir+"\n tmp_dir: "+tmp_dir+"\n threshold: "+threshold)
        env_setup()
        env_dir_check()
        process()
        
     else:
        print("ERROR: Invalid Args length !!!")
        print (">>>>Usage:<project dir> <tmp_path> <threshold(0 to 0.99)>")
        for i in argv:
            print (i+"\n")
        exit(1)
