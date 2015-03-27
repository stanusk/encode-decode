import os
from random import randint
from shutil import copy

pwd = os.getcwd()                 # absolute path to current folder
source = pwd + '/alphabet/'       # absolute path to pictures of alphabet
dest = pwd + '/message/'          # absolute path to folder with message

abc = [chr(n) for n in range(ord('a'), ord('z')+1)]   # list of letters in alphabet
abc.extend(['.', ' '])                                # add entries for "." and " "

sorted_source = sorted([n for n in os.listdir(source) if not n.startswith('.')])  # alphabetically sorted list of items 
                                                                                    # in source folder (pics of alphabet)

letters = dict(zip(abc, sorted_source)) # create dictionary mapping pictures to alphabet

# following procedure takes message entered by user and creates copies of related pictures in destination folder
# each copy starts with a random number (0-99) to encode the message
def encode():
  message = raw_input('\nEnter a message to encode:\n').lower()     # store message in lowercase

  for old_file in os.listdir(dest):         # clear content of dest folder
    os.remove(dest + old_file)

  for l in message:
    old_name = letters[l]                             # find letter in dict
    old_path = source + old_name                      # create path to letter in source folder

    part_name = str(len(os.listdir(dest))) + '.jpg'   # part name based on sequential number of the letter in message
    new_name = str(randint(0,99)) + '-' + part_name   # full name including random encoding
    new_path = dest + new_name                        # destination path
    
    copy(old_path, new_path)      # create copy of source file in dest folder with new name

  print 'Message: "%s" encoded in %s' %(message, dest)    # print confirmation


def decode():                         # short procedure to remove the encoding
  for f in os.listdir(dest):
    new_name = f[f.index('-')+1:]
    os.rename(dest+f, dest+new_name)


# very basic shell user interface
a = 'y'
while a == 'y':
  action = raw_input('\nEnter "e" to encode, "d" to decode, "x" to exit:\n')
  if action == 'e':
    encode()
  elif action == 'd':
    decode()
  else:
    break
  
  a = raw_input('\nEnter "y" for another operation or "x" to exit:\n')
