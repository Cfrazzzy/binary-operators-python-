#functionality of this program
#is to provide a right bitshift
#and then output a binary amount based
#off of the bitshift and starting amount


#xorfunc by conrad franke
#created Wednesday June 15th
#The purpouse is to take 
#in 2 parameters and then bit
#shift to the right b places
#and provide the binary value
#after bitshift
def bitshiftright(a,b):
    a = a >> b
    return a 
      
#"main"
answer = ""   
byte1 = int(input("input a to bitshift:"))
byte2 = int(input("input b to bitshift right # of places:"))
answer=bitshiftright(byte1,byte2)
answer = bin(int(answer))[2:].zfill(8)
print("numerical value is:")
print(int(answer,2))
print("binary value is: ")
print(answer)
print("chr value is:")
answer=int(answer,2)
print(chr(answer))
