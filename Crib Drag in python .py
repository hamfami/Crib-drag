# NAME : MUHAMAD ILHAM FAHMI BIN AZMI
# MATRIX : B021910022

import binascii 
from pickle import TRUE

BITS = ('0', '1')
ASCII_BITS = 7

def display_bits(b):
    """converts list of {0, 1}* to string"""
    return ''.join([BITS[e] for e in b])

def seq_to_bits(seq):
    return [0 if b == '0' else 1 for b in seq]

def pad_bits(bits, pad):
    """pads seq with leading 0s up to length pad"""
    assert len(bits) <= pad
    return [0] * (pad - len(bits)) + bits
        
def convert_to_bits(n):
    """converts an integer `n` to bit array"""
    result = []
    if n == 0:
        return [0]
    while n > 0:
        result = [(n % 2)] + result
        n = int(n / 2)
    return result

def string_to_bits(s):
    def chr_to_bit(c):
        return pad_bits(convert_to_bits(ord(c)), ASCII_BITS)
    return [b for group in 
            map(chr_to_bit, s)
            for b in group]

def bits_to_char(b):
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        value = (value * 2) + e
    return chr(value)

def list_to_string(p):
    return ''.join(p)

def bits_to_string(b):
    return ''.join([bits_to_char(b[i:i + ASCII_BITS]) 
                    for i in range(0, len(b), ASCII_BITS)])

def otp(m, k):
    assert len(m) == len(k)
    return [(mm + kk) % 2 for mm, kk in zip(m, k)]

def bin_to_hex(str1):
    bytes_str = bytes(str1, 'utf-8')
    return binascii.hexlify(bytes_str)

def XOR(A, B):
    return ''.join([chr(x ^ y) for x, y in zip(bytes(A, 'ascii'), bytes(B, 'ascii'))])

def crib_drag(text, c):
    for i in range(0, len(text) - len(c) + 1):
        pt = text[i:(i + len(c))]
        print("\t{0}:{1}".format(i,XOR(pt,c)))

#start

k= "ABCDEFGHIJKLMNOPQ"
m1 = "THE FIRST PROGRAM"
m2 = "HELLO CRUEL WORLD"

print ("\n")
print ("KEY\t\t: " + k )
print ("M1\t\t: " + m1 )
print ("M2\t\t: " + m2 )

m1bin = string_to_bits(m1)
m2bin = string_to_bits(m2)
keybin = string_to_bits(k)

display_m1bin  = display_bits(m1bin)
display_m2bin  = display_bits(m2bin)
display_keybin = display_bits(keybin)

C1 = otp(m1bin, keybin)           
C2 = otp(m2bin, keybin)           

print ("\n")
print ( "ENCRYPTION" )
print ("\n")

C1hex= bin_to_hex(bits_to_string(C1))                              
C2hex= bin_to_hex(bits_to_string(C2))

display_C1 = display_bits((C1))
display_C2 = display_bits((C2))

OTP = otp ( C1 , C2 )                                         
OTPhex = bin_to_hex(bits_to_string(OTP))

print ("Key\t\t: " + display_keybin)             
print ("M1 in bin\t: " + display_m1bin)    
print ("C1\t\t: " + display_C1)                        
print ("C1 in hex\t: " + C1hex.decode('utf-8'))                 

print ("\n")
print ("Key\t\t: " + display_keybin)         
print ("M2 in bin\t: " + display_m2bin)   
print ("C2\t\t: " + display_C2)                        
print ("C2 in hex\t: " + C2hex.decode('utf-8'))                 

print ("\n")
print ("otp(C1,C2 in bin\t: " + display_bits(OTP))                  
print ("otp(C1,C2) in hex \t: "+ OTPhex.decode('utf-8'))

print ("\n")
print ( "DECRYPTION" )
print ("\n")

C1C2 = XOR(m1, m2)

while(TRUE):
    print("Input Common words : ")
    guess = input()
    crib_drag(C1C2, guess)            
