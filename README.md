# mit-crypto-two-time-pad

Found this fun puzzle to solve in an MIT free computer network+security course: 6-857-network-and-computer-security-spring-2014 

Problem 1-2. One-time pad with ciphertext feedback: 
(a) Here are two 8-character English words encrypted with the same “one-time pad”. What are the words? 

e9 3a e9 c5 fc 73 55 d5
f4 3a fe c7 e1 68 4a df

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-857-network-and-computer-security-spring-2014/assignments/MIT6_857S14_ps1.pdf

My solution is not the most elegant, but works via XORing the 2 ciphertexts, and using dictionary attack of 8 letter words XOR'd with this key.  To get these 8 letter words I parsed a dictionary file found at https://github.com/dwyl/english-words. 

I did have trouble figuring out which message was which. It seemed there would be no logical way to tell, the professors answer confirmed this.
