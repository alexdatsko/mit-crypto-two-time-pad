f=open("words.txt","r")
f2=open("word8.txt","a")

def ascii(c):
  ch=ord(c)
  if (ch>64 and ch<91) or (ch>96 and ch<123):
    return 1
  else:
    return 0

word=f.readline()
while word:
  badword=0
  if len(word)==9:   #8 + end char
    for c in range(len(word)):
      if not (ascii(word[c])):
         pass
#        badword=1
#        break
    if not badword:
      print(word)
      f2.write(word)
  word=f.readline()

f.close()
f2.close()
