/*
sidb95
sbhatore95@gmail.com
basic_smileys
*/

# smileys in a file, smileys.txt

import os

def basic_smileys(void):
  hairs = ['l', '1', '|', '(', ')']
# three kinds of haircuts
  eyes = ['B', ':', ':$', ':§', ':•']
# three kinds of eyes
  noses = ['-', '--', '+', '++', '=']
# four kinds of noses
  mouths = ['$', '#', '@', 'π', 'o']
# four kinds of mouths
  f.open("smileys.txt", 'w')
  for hair in hairs:
    for eye in eyes:
      for nose in noses:
        for mouth in mouths:
          f.write(hair+eye+nose+mouth)
          f.write("\n")
  f.close()
  return
  
