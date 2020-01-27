
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
    count = 1
    for item in range(1,9):
        if item == 1 or item == 2 or item % 2 != 0:
            if num % item == 0:
                count += 1
            if count > 1:
                return False
    return True

    """returns True if a prime number and False if NOT a prime number"""
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

    if list == []:
        return 0

    for num in list:
        if isPrime(num) == True and num == digit:
            primelist.append(num)

    return primelist