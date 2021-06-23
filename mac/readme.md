

# cpu and memory command:

      system_profiler SPHardwareDataType | grep "  Memory:"
      system_profiler SPHardwareDataType | grep Cores:
      system_profiler SPHardwareDataType | grep Processors:

      #or, if you want to go low-level, use sysctl:

      sysctl hw.memsize
      sysctl hw.ncpu

      #btw, there are a bunch of other interesting things you can get from sysctl. Try:

      sysctl -a | grep cpu



Mac open two eclipse instances
- go to installation dir in terminal , cd /Users/user1/workspace/softwares/repo/eclipse_dump/
-  run command "open -n Eclipse.app/"



Text editors:

BBEDIT :
  JSON Formatter: [Link : https://gist.github.com/chales/510c5bed59a32ed0cb55]
  
              2016/03/15
            Tested with BBEdit 11.5 / OS X 10.11.3 / Python 2.7.10

            http://grokin.gs/blog/elegant-json-pretty-print-for-bbedit/

            Place the script (or a link to this script) in the ~/Library/Application Support/BBEdit/Text Filters directory
            Restart BBEdit.
            The new filter should be under: "Test > Apply Text Filter > bbedit-pretty-json"
            
            #content of file to be placed 
             bbedit-pretty-json.sh
            #!/bin/bash
            python -c "import sys, json; print json.dumps(json.load(sys.stdin), indent=2)"
