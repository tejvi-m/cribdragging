# a simple array implementation of a Linear Feedback Shift Register to generate pseudo random keys
# current implementatation takes in a 16 bit seed and a pseudo random bit string of length of the bin repr of the string.
# also xors the message with the pseudo random key.
# written in May 2017

plaintext=(input("enter the message: "))
lnr=list(input("enter the (16-bit) seed: "))[:16]
bin_pt=''
for ch in plaintext:
    bin_pt+=str(bin(ord(ch)))[2:]
key_len=len(bin_pt)
def lb(rl,l,n):
    if len(rl)==n:
        return(rl)
    rl.append(l[15])
    l11=[]
    x=bin(int(l[15],2)^int(l[13],2))
    x1=bin(int(x,2)^int(l[12],2))
    x2=bin(int(x1,2)^int(l[10],2))
    l11.append(x2[2:])
    for i in l[:-1]:
        l11.append(i)
    return lb(rl,l11,n)
def a(l):
    s=''
    for i in l:
        s=s+i
    return s

prk=(a(lb([],lnr,key_len)))
ciphertext=bin(int(prk,2)^int(bin_pt,2))[2:]
print(ciphertext)
