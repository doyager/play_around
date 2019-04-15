

#reading file content
file1_content=$(cat $file1)

# read file content and drop empty lines and drop lines starting with #
file1_content=$(grep . $file1 | grep "^[^#]")



#grep cmds

      # will drop/filter empty line
      grep . input.txt  

      # will drop/filter lines starting with #
      grep "^[^#]" input.txt


#tr cmd

      #delete spaces / white spaces
      
      cat input.txt | tr -d " "


# disk space 

  #at parent dir level , -s sums up
  du -skh /home/mac
  
  # to give all sub dir and files under a path
  du -kh
  
  # disk space free home
  df -khu /home/mac
  

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
