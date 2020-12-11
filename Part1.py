
#Primitive Types:
# integers ---> int() tam sayılar 1
# floats   ---> float() kesirli sayılar
# characters:
#            ord() Herhangi bir karakterin integer değerini verir
#            chr() ASCII tablosuna göre herhangi bir integer'in harf değerini verir

integer = 1
print(integer)

floats = 1.0
print(floats)

charToInt =  ord("A")
print(charToInt)

intToChar = chr(charToInt)


#Reference types
#strings ----> str() düz yazı ASCII tablosuna göre

stringEx1 = "Kerem"
stringEx2 = "çok"
stringEx3 = "yakışıklı"

print(stringEx1 + stringEx2 + stringEx3)

#####################- Tip Dönüşümleri -##########################

x = 5 #  5 ----> integer

intToFloat = float(x)

intToString = str(x)

intToInt = int(x) #That's actually useless :P

#####################- Değer değiştirme -#########################

y = 5

y = y + 5

print(y)

y = y / 5

print(y)




