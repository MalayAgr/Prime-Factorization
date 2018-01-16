from functools import reduce
from math import sqrt

#generator function to generate infinite prime numbers
def generatePrimeNumbers():

    #starts with smallest prime
    number  = 2
    c = 0

    while True:

        #no even number greater than 2 is prime
        #neglects all such numbers
        if not (number % 2 == 0 and number > 2):

            #our numbers will be odd
            #they will never have an even divisor
            #so, only taking odd divisors
            #also, we are likely to find a factor within the square root of the number
            #as any number n = (n*n)^(1/2)
            for divisor in range(3, int(sqrt(number))+1, 2):

                #checks whether number is divisible by anything other than itself and 1
                #setting a flag, c, to 1 if true
                if number % divisor == 0:
                    c = 1
                    break

            #if flag is not 1, it means the number is prime
            #thus, yields it
            if  c != 1:
                yield number

        #increasing the number
        number += 1

        #resetting the flag
        c = 0

#function which returns the prime factors of a number in a list
def getPrimeFactors(multiple):

    #getting prime numbers from the generator
    primeNumbers = generatePrimeNumbers()

    #initializing empty list to store prime factors
    output = []

    #the final division will decrease the number to 1
    #we need to stop there
    while multiple > 1:

        #getting a prime number using next() function
        factor = next(primeNumbers)

        #checks whether prime number is a factor of the number
        if multiple % factor == 0:

            #if true, adds it to the list
            output.append(factor)

            #divides the number to get the number for the next step
            multiple /= factor

            #reinitializes the prime numbers
            #because a number can be divisible by the same prime number again
            primeNumbers = generatePrimeNumbers()

        #if not, continues
        else:
            continue

    #returning the list
    return output

def main():

    repeat = True

    #setting an infinite loop
    #so that user can factorize as many numbers as they want
    while repeat:

        #taking input in a float variable
        try:
            number = float(input("\nEnter the number to be factorized: "))

        except IOError:
            print("\nPlease enter an integer value.")

        #if input was successful, does this
        else:

            #passes the number to the function above
            primeFactors = getPrimeFactors(number)

            #if the number of factors is more than 1
            #uses reduce to print them as: 2 x 2 x 3 x ...
            if len(primeFactors) > 1:
                print("\nThe prime factorization is: %s" %reduce(lambda x, y: str(x) + ' x ' + str(y), primeFactors))

            #if only one factor (meaning number is prime)
            #simply prints it
            else:
                print("\nThe prime factorization is: %s" %primeFactors[0])

            #asks user whether they would like to factorize another number
            #if no, sets repeat to False
            if not input("\nWould you like to factorize another number? ").lower().startswith('y'):
                repeat = False


if __name__ == '__main__':
    main()
