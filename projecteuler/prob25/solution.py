
import math

def solution(ndigits):

 i = 1
 j = 1
 index = 2
 while True:

  j = j+i
  i = j-i
  index += 1

  digits = int(math.log10(j))+1
  #print("i={}, j={}, ndig={}".format(i,j,digits))
  
  if (digits >= ndigits):
   break
 
 return j,index
