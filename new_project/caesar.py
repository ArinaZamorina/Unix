def caesar(text, shift): 
  cipher = ""
  for i in text:
    if i.isalpha():
      result = ord(ch) + shift 
      if result > ord('z'):
        result -= 26
      result_phrase = chr(result)
      cipher += result_phrase
  print cipher
  return cipher

from random import randint
key=''
keys=''
final=''
mes = input("cipher: ")
for symbol in mes:
    key = randint(0,32)
    keys += str(key) + "/"
    final += chr((ord(symbol) + key - 17)%33 + ord('А'))
print('Зашифрованное сообщение: ', final)
print ('Ключ шифрования: ',keys)
