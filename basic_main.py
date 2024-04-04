/*
sidb95
basic_main
sbhatore95@gmail.com
04.04.2024
*/

def firstHundredOnePercentages(void) {
  f.open("HundredAndOnePercentages.txt")
  for i in range(0..101):
      f.write(i)
      f.write("%\n")
  f.close()
  return


        