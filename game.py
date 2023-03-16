from random import choice, randrange
from datetime import datetime


operators = ["+", "-","*","/"]
times = 5
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
correct = 0
incorrect = 0
for i in range(0, times):    
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?") 
    match operator:
        case "+": 
            res = number_1 + number_2
        case "-":
            res = number_1 - number_2
        case "*":
            res = number_1 * number_2
        case "/":
            res = number_1 / number_2        
    result = input("resultado: ")
    if  int (result) == res:
        print("Correcto")
        correct += 1
    else:
        print("Incorrecto")
        incorrect += 1       
end_time = datetime.now()
total_time = end_time - init_time
print(f"\n Tardaste {total_time.seconds} segundos. Con {correct} aciertos y {incorrect} desaciertos")  
