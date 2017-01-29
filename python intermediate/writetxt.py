textfile = 'this is a new file\n written in a new file'

savefile = open('writefile.txt','w')
savefile.write(textfile)
savefile.close()