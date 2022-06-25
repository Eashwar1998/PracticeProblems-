sentence = input()
index = 0
final=""
prevIndex = 0
for character in sentence:
    index = index+1
    if (character.isupper() and index>1):
       final = final+sentence[prevIndex:index-1]+"_"
       prevIndex = index-1
    
final=final+sentence[prevIndex:]    
print(final.lower())
        
        
        
         
        
        
        