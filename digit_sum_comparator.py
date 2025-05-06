best_sum=0
lowest_sum=0
best_nums=[]
lowest_nums=[]
for i in range(3):
    num1=int(input("enter a number:"))
    dahganper=num1//10
    yekanper=num1%10
    sumper=dahganper+yekanper
    if best_sum==0 or sumper>best_sum:
        best_sum=sumper
        best_nums=[num1]    
    elif sumper == best_sum:
        best_nums.append(num1)
        print("Tie detected for best sum.")    
    if lowest_sum==0 or lowest_sum>sumper:
            lowest_sum=sumper
            lowest_nums=[num1]   
    elif sumper == lowest_sum:
        lowest_nums.append(num1)
        print("Tie detected for lowest sum.")           
print("the number with the greatest sum of digits is:",best_nums,best_sum)    
print("the number with the lowest sum of digits is:",lowest_nums ,lowest_sum)        
