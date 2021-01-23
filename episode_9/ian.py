import time
start = time.time()


cipher_file = open('p059_cipher.txt', 'r')
cipher_text = cipher_file.read()
char_list = cipher_text.split(',')

def XOR(chars,key): # key = 'exp' aka [101,120,112]
    result = []
    for i in range(0,int(len(chars)/len(key))*len(key),len(key)):
        for j in range(len(key)):
            result.append(chr(int(chars[i+j]) ^ ord(key[j])))
            
    # extra
    for i in range(len(chars)%len(key)):
        result.append(chr(int(chars[-(i+1)]) ^ ord(key[-(i+1)])))
    
    return result

print(f'Text: \n{"".join(XOR(char_list,"exp"))}\n')
print(f'Ans = {sum([ord(i) for i in XOR(char_list,"exp")])}')


end = time.time()
print(end-start)
