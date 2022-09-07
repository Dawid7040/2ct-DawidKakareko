def zadania1(numbers:list, k:int):
    tester = numbers.copy()
    debug = 0
    for i in range(len(numbers)):
        for j in range(len(tester)):
            debug += 1
            print(debug)
            if numbers[i] + tester[j] == k and not i==j:
                return True
        tester.pop(0)
    return False

print(zadania1([5,7,4,4], 10))

def zadanie2(str1):
    
    if not str1:
        return ""

    short_str = min(str1,key=len)

    for i, char in enumerate(short_str):
        for other in str1:
            if other[i] != char:
                return short_str[:i]

    return short_str 


def zadania3(actions:list):
    min_buy = min(actions)
    max_buy = max(actions)
    records = (0,0,0)
    for i in range(len(actions)): # Buy
        for j in range(len(actions)): # Sell
            if actions[j] - actions[i] <= 0: 
                continue
            if actions[j] - actions[i] > records[2] and  j > i: 
                records = (actions[i], actions[j], actions[j] - actions[i])
    return records

print(zadania3([20,10,13,17,15]))
            
