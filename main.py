
import random


COLORS = ['black', 'white', 'green', 'yellow']
MONEY_REQUIRED = 1

def get_slots() -> list[str]:
    return [random.choice(COLORS) for _ in range(4)]


def get_prize(slots:list[str], machine_money) -> int:
    if len(set(slots)) == 1:
        return machine_money
    if len(set(slots)) == 4:
        return machine_money/2
    
    for i in range(len(slots)-1):
        if slots[i] == slots[i+1]:
            to_pay = MONEY_REQUIRED * 5
            if to_pay > machine_money:
                return machine_money - to_pay
            return to_pay
    return 0 


def game_loop():
    machine_money = 10000
    money = 1000
    while money > MONEY_REQUIRED:
        
        slots = get_slots()
        prize = get_prize(slots, machine_money)
        
        if prize == machine_money:
            return machine_money
        elif prize < machine_money:
            money -= MONEY_REQUIRED
            machine_money += MONEY_REQUIRED
        elif prize < 0:
            return prize
    
    return 0


if __name__ == "__main__":

    result = game_loop()
    if result > 0:
        print('Money Gained: ', result)
    else:
        print(f'You got{result} free plays')

