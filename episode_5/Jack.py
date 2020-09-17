#Full disclosure, I had to look this up.
import time
import winsound
import threading as th

S = time.time()
def play():
    winsound.PlaySound('jazz.wav', winsound.SND_ALIAS)
check = True
while check == True:
    thread = th.Thread(target = play)
    thread.start()
    time.sleep(3)
    print('hello...')
    time.sleep(3)
    print("it's nice to meet you...")
    time.sleep(3)
    print("I hear the you're solving a problem...")
    time.sleep(3)
    print("maybe I could help you out?")
    time.sleep(3)
    print("Is this the problem you're trying to solve?")
    print("'How many different ways can 2 pounds be made using any number of coins?'")
    print("your answer: yes or no? ")
    YN = input()
    if YN == 'no':
        time.sleep(3)
        print("sorry I can't help then... goodbye.")
    else:
        time.sleep(3)
    print("fantastic! I know how to solve that one!")
    time.sleep(3)
    print("If I recall correctly, all you have to do is run this code:")
    code = '''target = 200
    coins = [1,2,5,10,20,50,100,200]
    ways = [1] + [0]*target
    for coin in coins:
        for i in range(coin, target+1):
            ways[i] += ways[i-coin]
    print(ways[target]) '''
    print(code)
    time.sleep(3)
    print("what's the matter?")
    time.sleep(3)
    print("are you having trouble running the code?")
    time.sleep(3)
    print("let me get that for you then.")
    target = 200
    coins = [1,2,5,10,20,50,100,200]
    ways = [1] + [0]*target
    for coin in coins:
        for i in range(coin, target+1):
            ways[i] += ways[i-coin]
    print(ways[target])

    time.sleep(3)
    print("you're welcome.")
    time.sleep(3)
    print("looks like its time for me to go, see you soon. enjoy the music")
    break

E = time.time()
print(E-S)

#make sure you have the .wav saved as jazz.wav in the same file location. 
