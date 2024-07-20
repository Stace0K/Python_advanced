# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

# Задача с банкоматом
# У вас есть банковская карта с начальным балансом равным 0 у.е.
# Вы хотите управлять этой картой, выполняя следующие операции,
# для выполнения которых необходимо написать следующие функции:
# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта.
# withdraw(amount): Снятие денег.
# exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.

import argparse
import logging

MULTIPLICITY = 50
PERCENT_REMOVAL = 0.015
MIN_REMOVAL = 30
MAX_REMOVAL = 600
PERCENT_DEPOSIT = 0.03
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = 0.1
RICHNESS_SUM = 10_000_000

bank_account = 0
count = 0
operations = []

FORMAT = '{levelname:<8} - {asctime} - {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.INFO, filemode='a', filename='bank_log.log',
                    encoding='utf-8')
logger = logging.getLogger('__name__')


def check_multiplicity(amount: int):
    """Функция проверяет сумму на кратность 50."""
    try:
        if amount % MULTIPLICITY == 0:
            logger.info('The amount is a multiple of 50 c.u.')
            return True
        else:
            logger.error('The amount is not a multiple of 50 c.u.')
            return False
    except Exception as e:
        logger.error(f'Function check_multiplicity error: {str(e)}')


def deposit(amount: int):
    """Функция пополнения счета."""
    try:
        global bank_account, count
        if check_multiplicity(int(amount)):
            bank_account += int(amount)
            print(f'A deposit of {amount} c.u. Current balance: {bank_account} c.u.')
            operations.append(f'A deposit of {amount} c.u. Current balance: {bank_account} c.u.')
            logger.info(f'A deposit of {amount} c.u. Current balance: {bank_account} c.u.')
            count += 1
        else:
            print('The amount should be a multiple of 50 c.u.')
            logger.error('The amount should be a multiple of 50 c.u.')
    except Exception as e:
        logger.error(f'Function deposit error: {str(e)}')


def withdrawal(amount: int):
    """Функция снятия средств со счета."""
    try:
        global bank_account, count
        if not check_multiplicity(int(amount)):
            print('The amount should be a multiple of 50 c.u.')
            logger.error('The amount should be a multiple of 50 c.u.')
            return False
        withdrawal_fee = (int(amount) * PERCENT_REMOVAL)
        if withdrawal_fee < MIN_REMOVAL:
            withdrawal_fee = MIN_REMOVAL
        elif withdrawal_fee > MAX_REMOVAL:
            withdrawal_fee = MAX_REMOVAL
        withdrawal_amount = (int(amount) + withdrawal_fee)
        if bank_account >= withdrawal_amount:
            bank_account -= withdrawal_amount
            print(
                f'A withdrawal of {amount} c.u. Withdrawal fee is {withdrawal_fee} c.u. Current balance: {bank_account} c.u.')
            operations.append(
                f'A withdrawal of {amount} c.u. Withdrawal fee is {withdrawal_fee} c.u. Current balance: {bank_account} c.u.')
            logger.info(
                f'A withdrawal of {amount} c.u. Withdrawal fee is {withdrawal_fee} c.u. Current balance: {bank_account} c.u.')
            count += 1
        else:
            print(
                f'Insufficient funds in your account. The amount with a fee is {withdrawal_amount} c.u. Current balance: {bank_account} c.u.')
            operations.append(
                f'Insufficient funds in your account. The amount with a fee is {withdrawal_amount} c.u. Current balance: {bank_account} c.u.')
            logger.error(
                f'Insufficient funds in your account. The amount with a fee is {withdrawal_amount} c.u. Current balance: {bank_account} c.u.')
    except Exception as e:
        logger.error(f'Function withdraw error: {str(e)}')


def exit():
    """Функция выхода, вывод итоговой информации о состоянии счета и выполненных операциях."""
    try:
        global bank_account
        if bank_account > RICHNESS_SUM:
            wealth_tax = round(bank_account * RICHNESS_PERCENT, 2)
            bank_account -= wealth_tax
            print(f'A wealth tax of {RICHNESS_PERCENT}% is {wealth_tax} c.u. Current balance: {bank_account} c.u.')
            operations.append(
                f'A wealth tax of {RICHNESS_PERCENT}% is {wealth_tax} c.u. Current balance: {bank_account} c.u.')
            logger.info(
                f'A wealth tax of {RICHNESS_PERCENT}% is {wealth_tax} c.u. Current balance: {bank_account} c.u.')
        operations.append(f'Take your card back, please. Current balance: {bank_account} c.u.')
        print(operations)
    except Exception as e:
        logger.error(f'Function exit error: {str(e)}')


def bank_parser():
    """
    Функция запуска из командной строки с передачей параметров.
    Запуск после перехода в соответствующую директорию: python Final_task.py <--параметр> <значение>
    """
    parser = argparse.ArgumentParser(description='The list of bank transactions.')
    parser.add_argument('--deposit', type=int, help='A deposit transaction.')
    parser.add_argument('--withdrawal', type=int, help='A withdrawal transaction.')
    parser.add_argument('--exit', help='Exiting the program: user`s account current balance and the list of '
                                       'transactions output.')
    args = parser.parse_args()
    dp = args.deposit
    wd = args.withdrawal
    deposit(dp)
    withdrawal(wd)


if __name__ == '__main__':
    bank_parser()

while True:
    mode = int(input('Please, choose an option: 1 - Deposit, 2 - Withdrawal, '
                     '3 - Check your current balance and transactions, exit' + '\n'))
    if mode == 1:
        summ = int(input('Enter the amount of deposit (digits only): '))
        check_multiplicity(summ)
        deposit(summ)
    elif mode == 2:
        summ = int(input('Enter the amount of withdrawal (digits only): '))
        check_multiplicity(summ)
        withdrawal(summ)
    elif mode == 3:
        exit()
        break
    else:
        print('There is no such an option. Try again.')
