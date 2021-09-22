def boi(a, b):
    if a > b:
        print("the largest is a =  ", a)

    else:
        print("the largest is  b =   ", b)


boi(12, 18)


def peaky(x, y, z):
    if x > y and x > z:
        print("the largest among three is  =   ", x)
    elif y > x and y > z:
        print("The largest value among three is =  ", y)

    else:
        print("the largest among three is =  ", z)


peaky(13, 17, 19)


def str_length(length):
    c = 0
    for i in length:
        c += 1

    print("the length of the string is  ", c)


length = "Ronaldo"

print(str_length(length))


def vowel(x):
    n = ""
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        print("vowel", x)
    else:
        print("this is not vowel")


n = input("enter the string ")
print(vowel(n))


def translate(word):
    new_word = ""
    consonant = "bcdefghklmnopqrstuvwxyzBCDEFGHKLMNOPQRSTUVWXYZ"

    for i in word:
        if i in consonant:
            new_word += i + 'o' + i
        else:
            new_word += i
    return new_word


trans = input("enter the word ")
print(translate(trans))


def boi(sum):
    lst = 0

    for i in sum:
        lst += i
    return lst


def multiply(sum):
    lst = 1
    for i in sum:
        lst = lst * i
    return lst


print(boi([1, 2, 3, 4, 5]))
print(multiply([1, 2, 3, 4, 5]))


def reverse(x):
    return x[::-1]


x = "fool"
print(reverse(x))


def plaindrome(string):
    return string == string[:: -1]


print(plaindrome("abc"))
print(plaindrome("radar"))
print(plaindrome("12321"))


def member(y, a):
    if len(a) == 0:
        return False
    return y == a[0] or member(y, a[1:])


print(member(12, ["bass", 12]))
print(member(12, [12, 'a']))
print(member(4, ['a,b,c']))


def generate_char(x, str):
    result = ''
    for i in range(x):
        result += str
    return result


print(generate_char(5, '&'))
print(generate_char(4, '#'))
print(generate_char(3, '@'))
