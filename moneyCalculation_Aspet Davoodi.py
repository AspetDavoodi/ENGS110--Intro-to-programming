def calcCurrYearMoney (money, percent):
    decimalPercent = percent/100
    decimalPercent = decimalPercent + 1
    money = money * decimalPercent
    return (money)
    


def main ():

    print ("~~Hello! This is a program to help you calculate your final balance in your account \n after the number of years and initial amount of money you specify.~~")

    initMoney = int ( input ("How much money did you store in your account (Integer number)"))
    interestPercent = int ( input ("What is the interest rate percentage of your account? (integer number without % symbol- e.g. 50 or 10)"))
    yearsInBank = int ( input ("Integer between 1 and 20, number of years?"))

    initValMoney = initMoney
    initValYears = yearsInBank


    while yearsInBank > 0:
        initMoney = calcCurrYearMoney (initMoney, interestPercent)
        yearsInBank = yearsInBank - 1

    
    print ("After", initValYears, "years, your initial money", initValMoney, "has become, you final balance", initMoney)

main ()
