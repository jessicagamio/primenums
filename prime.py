import unittest


### find prime number function

## prime number when it is a multiple of 1 and itself, all odd numbers except for2

## set a counter to equal 1
## from a range of 1 to 10
    # if num is 1 or 2 or odd
        # if num divisible by the given num 
            # add to counter
        # if counter greater than 1
            # return False
# return True
def isPrime(num):
    """returns True if a prime number and False if NOT a prime number"""

    # can only result from multiplie by itself and 1
    # can only be odd number exclude 2
    # can not be negative numbers
    if num <= 0:
        return False

    if num == 1 or num == 2:
        return True

    elif num % 2 != 0: # if odd number
        for item in range(2,9):
            if item == 2 or item % 2 != 0 and item != num:
                if num % item == 0:
                    return False
        return True






#################


## finding the 2nd digit of birthdate
# given birthdate(the format) for this 01152011
# convert to string
# slice 2nd digit
# convert to interger



def getDigit(birthdate):
    """returns the 2nd digit of birth date"""

    str_bdate = str(birthdate)
    str_bdate = str_bdate[1]

    return int(str_bdate)

    


### main function
# parameters list and date
# given a list of numbers return only a list prime nums that match the 2nd digit of birth date

#create prime list

#isolate the second digit

# iterate through the give list
    #if the num in list is not a prime num and equal to second digit
        #append to list


def makePrimeList(list, birthdate):
    primelist = []
    digit = getDigit(birthdate)

    if isPrime(digit) == False:
        return "2nd digit not a prime number"

    if list == []:
        return 0

    for num in list:
        if isPrime(num) == True and num == digit:
            primelist.append(num)

    return primelist


class testFunction (unittest.TestCase):
    def testMethod(self):
        self.assertEqual(makePrimeList([2,3,57,3], 13032019),[3,3])


if __name__=="__main__":
    unittest.main()