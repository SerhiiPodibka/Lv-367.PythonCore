def solution(number):
    for number in range(1,10):
    
        if(number%3==0 or number%5==0):
        
            number += number
            
    return number
