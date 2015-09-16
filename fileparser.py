import sys
import os

##########   WRITING FILE OUT   ##########
# #open file to write
to_write_file_pointer = open('to_read.txt', 'w+')
output_file_pointer = open('output.txt','w')

#FOR: number in range from 1 to 10, write the number and a new line to our file
for number in range(1, 10):
    to_write_file_pointer.write("{0}\n".format(number))

#create a list of letters to output to our file
letters = ['a', 'b', 'c', 'd', 'e']

#FOR: letter in letters from a to e, write letter and a new line to our file
for letter in letters:
    #write letter to file (with a new line)
    to_write_file_pointer.write("{0}\n".format(letter))

#close file
# to_write_file_pointer.close()

# Reset file pointer
to_write_file_pointer.seek(0)


##########   READING FILE IN   ##########
# #open file to read
# to_read_file_pointer = open('to_read.txt', 'r')

#FOR: line in to_read_file_pointer, read and print each line
for line in to_write_file_pointer:
    #print line
    print("Line: {0}".format(line))
    output_file_pointer.write("Line: {0}".format(line))

#uncomment line below to remove file after reading
#os.remove('to_read.txt')

#close file
to_write_file_pointer.close()
output_file_pointer.close()
raise SystemExit(0)
#ALL DONE!
