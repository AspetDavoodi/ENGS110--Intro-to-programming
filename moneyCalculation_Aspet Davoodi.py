def calcCurrYearMoney (money, percent):
    decimalPercent = percent/100 #turn given double digit percentage into decimal
    decimalPercent = decimalPercent + 1 #add 1 to make the percentage more than 100%
    money = money * decimalPercent #calculate change to input money
    return (money)
    


def main ():

    print ("~~Hello! This is a program to help you calculate your final balance in your account \n after the number of years and initial amount of money you specify.~~")

    initMoney = int ( input ("How much money did you store in your account (Integer number)"))
    interestPercent = int ( input ("What is the interest rate percentage of your account? (integer number without % symbol- e.g. 50 or 10)"))
    yearsInBank = int ( input ("Integer between 1 and 20, number of years?"))

    initValMoney = initMoney #store the initial value for input money for later use (such that no changes are applied to it)
    initValYears = yearsInBank #store the initial value for input years for later use (such that no changes are applied to it)


    while yearsInBank > 0: # main calculation
        initMoney = calcCurrYearMoney (initMoney, interestPercent) #calculate new value for each year
        yearsInBank = yearsInBank - 1 #for while loop to end

    
    print ("After", initValYears, "years, your initial money", initValMoney, "has become, you final balance", initMoney) #final prompt

main ()
