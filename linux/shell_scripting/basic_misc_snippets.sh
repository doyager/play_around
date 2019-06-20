


#check args length

#!/bin/sh
if [ "$#" -ne 1 ]; then
  echo "Usage: <date>" >&2
  exit 1
fi

#result of prev command 
 echo $?
