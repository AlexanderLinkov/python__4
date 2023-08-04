total = 0
count = 0
bonus = 0
nalog = 0
cash_log = []


def input_cash(money):
    if money % 50 == 0:
        global total; global count; global bonus; global nalog
        total += money
        count += 1
        cash_log.append(f'Пополнение баланса на: {money}')
        if count % 3 == 0:
            bonus = total * 0.03
            total += bonus
        else:
            bonus = 0
        if total > 5_000_000:
            nalog = total * 0.1
            total -= nalog
            return(f'Баланс пополнен на: {money}, вычтен налог: {nalog}, начислено бонусов: {bonus}, доступно на карте: {total}')
        else:
            return(f'Баланс пополнен на: {money}, начислено бонусов: {bonus}, доступно на карте: {total}')
    else:
        count += 1
        if total > 5_000_000:
            nalog = total * 0.1
            total -= nalog
            return(f"ОШИБКА! Введите купюры номиналом кратным 50 у.е., вычтен налог: {nalog}, Остаток на счете: {total}")
        else:
            return(f"ОШИБКА! Введите купюры номиналом кратным 50 у.е., Остаток на счете: {total}")
    

def output_cash(money):
    global total; global count; global bonus; global nalog
    if money % 50 == 0 and (total - money) >= 0: 
        total -= money
        cash_log.append(f'Снятие денег в размере: {money}')
        count += 1
        cash_back = money * 0.015
        if cash_back < 30:
            cash_back = 30
        elif cash_back > 600:
            cash_back = 600
        total -= cash_back
        if count % 3 == 0:
            bonus = total * 0.03
            total += bonus
        else:
            bonus = 0
        if total > 5_000_000:
            nalog = total * 0.1
            total -= nalog
            return(f'С баланса снято: {money}, процент за снятие: {cash_back}, вычтен налог: {nalog}, начислено бонусов: {bonus}, доступно на карте: {total}')
        else:
            return(f'С баланса снято: {money}, процент за снятие: {cash_back}, начислено бонусов: {bonus}, доступно на карте: {total}')
    else:
        count += 1
        if total > 5_000_000:
            nalog = total * 0.1
            total -= nalog
            return(f'С баланса снято: {money}, процент за снятие: {cash_back}, вычтен налог: {nalog}, начислено бонусов: {bonus}, доступно на карте: {total}')
        else:
            return(f"ОШИБКА! Укажите сумму снятия кратную 50 у.е. и не превышающую сумму остатка! Остаток на счете: {total}")


def exit():
    global count
    count += 1
    cash_log.append('Сеанс завершен!')
    return(f"Остаток денежных средств на карте: {total}, Сеанс завершен")


print(input_cash(100))
print(output_cash(50))
print(input_cash(500))
print(output_cash(150))
print(input_cash(5000000))
print(output_cash(300))
print(exit())
print(f'Кол-во операций по карте: {count}')
print(cash_log)