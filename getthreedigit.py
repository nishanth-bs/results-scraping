def digit(x):
    if(x<10):
        return(str(x%x)+str(x%x)+str(x%10))

    elif(x<100 and x>9):
        return(str(x%x)+str(x%100))

    else:
        return(x)

#digit(150)

#for i in range(1,10):
 #   j=(digit(i))
  #  print (j)
