




# disk space 

  #at parent dir level , -s sums up
  du -skh /home/mac
  
  # to give all sub dir and files under a path
  du -kh
  
  

#vi 


    # go line number
    
      #press Esc and then Shift-g 
      
    # go to last column of the line
    
       # shift + 4 or press $
      
   # go to first line
   
        # press gg
        
   # go to last line
   
        # Shift + G
        # Cntrl + End
        # 

    # find and replace

    :%s/search_string/replacement_string/g

    # delete empty lines 

        :g/^$/d
        #Here’s a brief explanation of how this vim “delete blank lines” command works:
        #The : character says, “put vim in last-line mode.”
        #The g character says, “perform the following operation globally in this file.” (Operate on all lines in this file.)
        #The forward slash characters enclose the pattern I’m trying to match. In this case I want to match blank lines, so I use the regular expression ^$. Here the ^ means “beginning of line,” and $ means “end of line,” so with no characters in between them, this vim regex means “blank line.” (If I had typed ^abc$, that would mean, “find a line with only the sequence of characters ‘abc’”.)
        #The d at the end of the command says, “When you find this pattern, delete the line.”
