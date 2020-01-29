def choose(n, k):
    #N choose K
    #Big! / Little! * (big-little)!
    if(k == 1):
        return n
    elif(k == 0 or n == k):
        return 1
    if(n > k):
        nFact = n
        kFact = k
        minus = n - k
        minusFact = n - k

        while(n > 1):
            n -= 1
            nFact *= n
        while(k > 1):
            k -= 1
            kFact *= k
        while(minus > 1):
            minus -= 1
            minusFact *= minus
        numerator = nFact
        denominator = kFact * minusFact
        num = int(numerator / denominator)
        return num
    else:
        print("The number you're trying to choose must be between 0 and the number you're choosing from.")

def intInputValidation(firstMessage, secondMessage):
    while True:
        try:
            n = int(input(firstMessage))
        except ValueError:
            print(secondMessage)
            continue
        else:
            break
    return n

def floatInputValidation(firstMessage, secondMessage, upper, lower):
    while True:
        try:
            n = float(input(firstMessage))
        except ValueError:
            print(secondMessage)
            continue
        if (n < lower or n > upper):
            print("The probability must be higher than " + str(lower) + ", and less than " + str(upper) + ".")
            continue
        else:
            break
    return n

n = intInputValidation("How many chances are there for the event to occur? ", "Sorry, that's not an integer.")
while True:
    try:
        r = intInputValidation("How many times does the desired event occur? ", "Sorry, that's not an integer.")
    except:
        r = intInputValidation("How many times does the desired event occur? ", "Sorry, that's not an integer.")
    if(r > n or r < 0):
        print("The amount of chances must be between 0, and " + str(n) + ".")
        continue
    else:
        break
p = floatInputValidation("What's the chance of the desired event occuring? ", "Sorry, that's not a float.", 1, 0)

print(str(choose(n, r) * float(p ** r) * float((1 - p) ** (n - r)) * 100) + "%")
