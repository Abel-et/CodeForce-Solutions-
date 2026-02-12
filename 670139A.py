test = int(input())

for i in range(test):
  size = int(input())
  s = input()

  
  arr = []
  n = len(set(s))
  if n < 3 :
    print('0' , "if l")
  else:
    print(s)
    for i in range(size-3):
      w = s[i:i+4]
      print(w, 'infor ')
      if w =='2026' and len(w)>2:
        print('0')
        break
      elif w != '2026' and len(w)>3:
        print('here')
        year = '2026'
        count = 0
        print(w,'in elif')
        for i in range(3):
          print('here elif for loop')
          if year[i] == w[i]:
            print(year[i], w[i])
          else:
            count +=1
        arr.append(count)
        arr.clear()
        print(min(arr),"elif")
        break
      
    
      
  

      
    
    
  