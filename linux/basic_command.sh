
# ip address from hostname 

ping -s `hostname`

PING nyk4035: 56 data bytes
64 bytes from nyk4035 (192.52.32.15): icmp_seq=0. time=0.186 ms

# nslookup `hostname`
nyk4035.unix.com       canonical name = nyk4035.unix.com
Name:   nyk4035.unix.com
Address: 192.52.32.15


#vi 

    # to view list of all setting
    
      # : set all
      
   # to view list of all setting we have ,
      # : set

    # set line number 
    
      # press : and say "set number" and enter 
      #:set number   
      
      # to remove line numbers
      # :set nonumber

    # go line number
    
      #press Esc , then press line number and then Shift-g 
      
    # go first char & got last char  MAC
    
    cntrl + a   - first char
    contrl + e   - last char 
    
    # go to last column of the line
    
       # shift + 4 or press $
       
    # go to nth character on a line
      # go to that particular line and press char number "example 256 character" and | and press enter
      # 256| and press enter
      
   # go to first line
   
        # press gg
        
   # go to last line
   
        # Shift + G
        # Cntrl + End
        # 



#reading file content
file1_content=$(cat $file1)

# read file content and drop empty lines and drop lines starting with #
file1_content=$(grep . $file1 | grep "^[^#]")


#search file
find <path> name=<file-name>

find . name=<file.txt>


#grep cmds

      # will drop/filter empty line
      grep . input.txt  

      # will drop/filter lines starting with #
      grep "^[^#]" input.txt


#tr cmd

      #delete spaces / white spaces
      
      cat input.txt | tr -d " "


# view logs using process id 

ps -aux | grep java-agent
tail -f /proc/<pid>/fd/1


# To check fire wall connectivity 

        #netcat
            nc -v <destination_host> <destination_host_port>

            To check firewall connection from serv1 to server2 on port 8089

            - log on to server1
            - the use command "nc -v server2 8089" 
            - We have to get verbose messages saying connection sucess.


            #netcat is a computer networking utility for reading from and writing to network connections using TCP or UDP.
            #The command is designed to be a dependable back-end that can be used directly or easily 
            #driven by other programs and scripts.



# get ipaddress 
    
    #1
    # login to that particular machine 
        ifconfig 
        look for eth0 and inet under that , inet is the ipaddress
        
        Eg : ifconfig
        eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 11.111.1.100  netmask 255.255.255.0  broadcast 11.111.6.255
      
     #2
     # login in to the machine 
      nslookup <hostname>
      Eg: nslookup dev_discovery_node
      
        Name:	dev_discovery_node.company.com
        Address: 11.111.1.100
        
       #3 
       #login and ping to the same host 
       ping <hostname>
       
       eg: hostname :  dev_discovery_node , ip : 11.111.1.100
         ping dev_discovery_node
        PING dev_discovery_node.compnay.com (11.111.1.100) 56(84) bytes of data.
        64 bytes from dev_discovery_node.company.com (11.111.1.100): icmp_seq=1 ttl=64 time=0.018 ms
        64 bytes from dev_discovery_node.company.com (11.111.1.100): icmp_seq=2 ttl=64 time=0.036 ms
        64 bytes from dev_discovery_node.compnay.com (11.111.1.100): icmp_seq=3 ttl=64 time=0.036 ms
        64 bytes from dev_discovery_node.company.com (11.111.1.100): icmp_seq=4 ttl=64 time=0.046 ms

        
# disk space 

  #at parent dir level , -s sums up
  du -skh /home/mac
  
  # to give all sub dir and files under a path
  du -kh
  
  # disk space free home
  df -khu /home/mac
  

# no of threads per core

            lscpu

            Thread(s) per core:    2

    # search 

          # to search 
            #/<search item>
          # to go next item 
            # press n
          # to go previous item
            # press N i.e. Shift + n
          # go to first occurance
            # ggn
          # go to last occurance
            # GN i.. shift + g + n
          # clear last search highlighting 
              # :noh
       
    # find and replace

    :%s/search_string/replacement_string/g

    # delete empty lines 

        :g/^$/d
        #Here’s a brief explanation of how this vim “delete blank lines” command works:
        #The : character says, “put vim in last-line mode.”
        #The g character says, “perform the following operation globally in this file.” (Operate on all lines in this file.)
        #The forward slash characters enclose the pattern I’m trying to match. In this case I want to match blank lines, so I use the regular expression ^$. Here the ^ means “beginning of line,” and $ means “end of line,” so with no characters in between them, this vim regex means “blank line.” (If I had typed ^abc$, that would mean, “find a line with only the sequence of characters ‘abc’”.)
        #The d at the end of the command says, “When you find this pattern, delete the line.”
        
        
        
        
        
        
        
  # set default permission for files and dir under a path 
  
          From the article:

        chmod g+s <directory>  //set gid 
        setfacl -d -m g::rwx /<directory>  //set group to rwx default 
        setfacl -d -m o::rx /<directory>   //set other
        Next we can verify:

        getfacl /<directory>
        Output:

        # file: ../<directory>/
        # owner: <user>
        # group: media
        # flags: -s-
        user::rwx
        group::rwx
        other::r-x
        default:user::rwx
        default:group::rwx
        default:other::r-x

