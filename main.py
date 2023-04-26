def twoCommonList(c, b):
    elementsInBothList = []
    for x in c:
        if x in b:
            elementsInBothList.append(x)

    return elementsInBothList


def PalindromeList(b):
    result = []
    for x in b:
        s_lower = x.lower()
        if s_lower == s_lower[::-1]:
            result.append(x)
    return result


def sieve_of_eratosthenes(numberList):
    primeList = []
    numberList = sorted(set(numberList))
    while numberList:
        primeNumber = numberList.pop(0)
        if primeNumber < 2:
            continue
        primeList.append(primeNumber)
        numberList = [number for number in numberList if number % primeNumber != 0]
    return primeList


def anagrams(x, xList):
    sorted_x = sorted(x.lower().replace(" ", ""))
    result = []

    for w in xList:
        sorted_a = sorted(w.lower().replace(" ", ""))
        if sorted_x == sorted_a:
            result.append(w)
    return result


listA = [5, 99, 53, 234, 531, 645, 96, 223]
listB = [77, 43, 99, 234, 5, 53, 645]
words = ["raufFuar", "Yatay", "Urla", "Edirne"]
numbers = [99, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
a = "listen"
anagramWords = ["enlists", "google", "inlets", "banana"]


commonList = twoCommonList(listA, listB)
print("part 1:")
print(commonList)


palindromeList = PalindromeList(words)
print("\npart 2:")
print(palindromeList)


primeNumbers = sieve_of_eratosthenes(numbers)
print("\npart 3:")
print(primeNumbers)


anagramList = anagrams(a, anagramWords)
print("\npart 4:")
print(anagramList)
