
import solution as sol

topnum = 28123

thesum,abundants,nonexpressable = sol.solution(topnum)

print("The sum of all integers under {} which can not be written as the sum of two abundant numbers is {}".format(topnum, thesum))
#print("The list of nonexpressable numbers < {} is:\n {}".format(topnum,nonexpressable))
#print("The list of abundant numbers < {} is:\n {}".format(topnum,abundants))
