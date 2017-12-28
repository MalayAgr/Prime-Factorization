from functools import reduce
from math import sqrt

def generatePrimeNumbers():

    number  = 2
    c = 0

    while True:

        if not (number % 2 == 0 and number > 2):

            for divisor in range(3, int(sqrt(number))+1, 2):

                if number % divisor == 0:
                    c = 1
                    break

            if  c != 1:
                yield number

        number += 1
        c = 0


def getPrimeFactors(multiple):

    primeNumbers = generatePrimeNumbers()
    output = []

    while multiple > 1:

        factor = next(primeNumbers)

        if multiple % factor == 0:
            output.append(factor)
            multiple /= factor
            primeNumbers = generatePrimeNumbers()

        else:
            continue

    return output

def main():

    repeat = True

    while repeat:
        try:
            number = float(input("\nEnter the number to be factorized: "))

        except IOError:
            print("\nPlease enter an integer value.")

        else:
            primeFactors = getPrimeFactors(number)

            if len(primeFactors) > 1:
                print("\nThe prime factorization is: %s" %reduce(lambda x, y: str(x) + ' x ' + str(y), primeFactors))

            else:
                print("\nThe prime factorization is: %s" %primeFactors[0])

            if not input("\nWould you like to factorize another number? ").lower().startswith('y'):
                repeat = False


if __name__ == '__main__':
    main()
