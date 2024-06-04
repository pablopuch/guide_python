### Regular Expressions ###

import re

# match

my_string = "Esta es mi cadena \nde texto Cadena"
my_other_string = "Esta es otra cadena de ejemplo Cadena"

# match = re.match("Esta es mi" , my_string, re.I)

# print(match)
# start, end = match.span()

# print(start)
# print(end)
# print(my_string[start:end])


# match = print(re.match("cadena" , my_other_string))
# # if not(match == None): otra forma de comprobar 
# if match != None:
#     print(match)
#     start, end = match.span()
#     print(my_string[start:end])
    
# print(re.match("Expresiones regulares", my_string))



# # search

# searche = re.search("Esta es mi" , my_string, re.I)

# print(searche)
# start, end = searche.span()
# print(my_string[start:end])




# findall

# findall = re.findall("cadena", my_string, re.I)
# print(findall)



# split 

# split = re.split("\n", my_string)
# print(split)




# sub 

# sub = re.sub("Cadena", "CADENA", my_string, re.I)
# print(sub)

    
    
    

# Patterns

pattern = r"[Cc]adena"
print(re.findall(pattern, my_other_string))

pattern = r"[Cc]adena|ejemplo"
print(re.findall(pattern, my_other_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_other_string))

email = "pablo@pablo.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))
