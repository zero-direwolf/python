appendtext = '\nthis is an anddition to the text file from write file'
appendfile = open('writefile.txt','a') 
appendfile.write(appendtext)
appendfile.close()