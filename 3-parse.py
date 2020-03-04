f=open("poss.txt","r")
f2=open("word8.txt","r")
f3=open("match.txt","a")

wordlist=f2.readlines()

word=f.readline()
while word:
  if word in wordlist:
    print(word)
    f3.write(word+"\n")
  word=f.readline()

f.close()
f2.close()
f3.close()
