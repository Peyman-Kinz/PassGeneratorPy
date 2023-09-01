import random

lower_case = "abcdefghijklmnopqrstuvwxyz" 
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "[]{}#()*;._-"

ans = lower_case + upper_case + num + symbol

lenght = 10
password = "".join(random.sample(ans, lenght))
print("Passwort wird generiert... Das passwort lautet: ",password)
