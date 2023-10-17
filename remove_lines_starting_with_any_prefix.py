file1 = open('YourTextFile.txt','r')
 
# defining object file2 to open YourTextFileUpdated file in write mode
file2 = open('YourTextFileUpdated.txt','w')
 
# reading each line from original text file
for line in file1.readlines():
   
     # reading all lines that do not begin with "YourPrefix"
    if not (line.startswith('YourPrefix')):
       
        # printing those lines
        print(line)
         
        # storing only those lines that 
        # do not begin with "YourPrefix"
        file2.write(line)
 
# close and save the files
file2.close()
file1.close()
