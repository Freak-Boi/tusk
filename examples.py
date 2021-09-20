# __________________________________ example to find the max of two ____________________________________________
#
# def largest(a,b):
#     print('the largest number is  ')
#
#     if a >= b :
#         print(a)
#     elif b >= a:
#         print(b)
#
#     else:
#         print("none")
#
# largest(4,5)
# largest(12,28)
# largest(50,2)
#
# ___________________________________ example to find max of 3 ___________________________________________
#
# def max(a,b,c):
#     print("the maximum number is")
#
#     if a > b and a > c:
#         print('a',a)
#     elif b > a and b > c:
#         print('b',b)
#     elif c > a and c > b :
#         print('c',c)
#     else:
#         print('none')
# max(4,56,7)
# max(6,4,3)
# max(12,23,77)

# __________________________ example 3 to find the length of the string ______________________________________
#
# def len_str(length):
#
#     c=0
#     for i in length:
#         c += 1
#     print("the length of the string is ",c)
# length = "ronaldo"
# print('the length of the string is  ' , len(length))
# print(len_str(length))


# ___________________________  example 4 to find the vowel from a character ____________________

# def vowel(x):
#     if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
#         return "True"
#     else:
#         return "False "
#
#
# a = input("Enter the letter :- ")
# print(vowel(a))

# -__-________________________ example 5  Swedish robert translator_____________________________
#
# def translate(word):
#     consonant = " bcdefghklmnopqrstuvwxyzBCDEFGHIJKLMNOPQRSTUVWXYZ"
#     new_word = ''
#     # vowels = "aeiouAeiou"
#     for i in word:
#         if i in consonant:
#             new_word += i + "o" + i
#         else:
#             new_word += i
#     return  new_word
#
#
# print("we can translated every word")
# trans = input("introduce , The word that u are want to translate  =  ")
# print("the translate word is  ", translate(trans))

# ______________________________ example 6 sum and mulitpy ---------------------_____________

# def sum(boi):
#     lst= 0
#     for i in boi:
#        lst += i
#     return lst
#
# def multipy(boi):
#     lst = 1
#     for i in boi:
#         lst = lst * i
#     return lst
#
#
# print(sum([1, 2, 3, 4, 5]))
# print(multipy([1, 2, 3, 4, 5]))

# __________________________ example 7 reverse the sting ______________________________________________

# def main_function(x):
#     return  x[::-1]
#
# txt = main_function("i am foool")
# print(txt)
#
# # _________________________ example 8 is a plaindrome ___________________________________________________
#
#
# def plaindrome(string):
#
#     return string == string[::-1]
#
# print(plaindrome("abc"))
# print(plaindrome("radar"))
# print(plaindrome("12321"))

# ______________________ example 9 is a member _________________________________________
#
# def member(x,a):
#     if len(a) == 0 :
#         return False
#     return x == a[0] or member(x,a[1:])
#
#
# print(member(12,["bass",12]))   # True
# print(member('8',['a']))    # False
# print(member(4, [2, 4]))    # False

# ______________________________  example 10 overlapping ______________________________________

#
# def overlapping(lst1, lst2):
#     print(lst1)
#     print(lst2)
#     for i in range(len(lst1)):
#         for j in range(len(lst2)):
#             if lst1[i] == lst2[j]:
#
#                 return True
#
#
# lst1 = ["aa", "bb", 'cc']
# lst2 = ["c", 9, "ee"]
#
# if overlapping(lst1,lst2):
#     print("overlapping is boomb_basket")
# else:
#     print(" no overlapping is done")

# # ____________________________ example 11 generate an char___________________________________________
#
# def generate_char(x ,str):
#     result = ""
#     for i in range(x):
#         result += str
#     return result
#
#
# print(generate_char(5, "x"))
# print(generate_char(6, "*"))
# print(generate_char(7, "&"))
#
# # ____________________________ example 12  historical graph  ___________________________________________________

#
# def historical(lst):
#     for n in lst:
#         print (n * "*")
#     print(10 * "-")  # Just to add some space between each test
# print("the graph can be shown .....", historical([3,3,5]))
# print("the graph can be shown .....", historical([4,2,5]))

# ________________________ example 13 max in the list ____________________________________________________________

# def max_list(lst):
#     max = 0
#     for i in lst:
#         if i > max :
#             max = i
#     return max
#
#
# print("the largest number in the list is ..............  ",max_list([12,13,14,1,15,14,1223,23131]))
# print("the largest number in the list is ..............  ", max_list([123, 234, 22, 122, 112]))

# ___________________________ example 14 words into integer ________________________________________
#
# def words_length(lst):
#     lenlist = [len(i) for i in lst]
#
#     return lenlist
#
#
# print("The length of the words that are written are following", words_length(['hello', 'peaky blinder']))
# print("the length of the words tha ara written are following ", words_length(['something is fleshy around here']))
