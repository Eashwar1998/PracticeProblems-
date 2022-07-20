first = input()
second  = input()
fl = len(first)
sl = len(second)
overlap = ""
first_index =-1
for i in range(fl-1,0,-1):
    if(first[i]==second[0]):
        first_index = i;
    

if first_index ==-1:
    print("No overlapping")
else:
    overlapping_length = fl-first_index;

    overlapping_string = first[first_index:]
  
    s = second[:overlapping_length]
  
    if (overlapping_string == s):
        print(s)
    else:
        print("No overlapping")
    
        
    
