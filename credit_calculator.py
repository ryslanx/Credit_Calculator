import math
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument("--type", help="indicates the type of payment: annuity or diff")
parser.add_argument("--principal", help="is used for calculating both types of payment." +
                    "You can get its value knowing the interest, the annuity payment, and the number of periods",
                    type=int)
parser.add_argument("--interest", help="is specified without the percentage sign",
                    type=float)
parser.add_argument("--payment", help="refers to the monthly payment",
                    type=int)
parser.add_argument("--periods", help="parameter denotes the number of months and/or years needed to repay the credit",
                    type=int)
args = parser.parse_args()  # saves all the variables from the command line
if len(sys.argv) != 5:
    print("Incorrect parameters")
    exit()
elif args.type != "annuity" and args.type != "diff":
    print("Incorrect parameters")
    exit()
elif args.type == "diff" and args.payment:
    print("Incorrect parameters")
    exit()
elif not args.interest:
    print("Incorrect parameters")
    exit()
if args.type == 'diff' and args.principal and args.periods and args.interest:
    credit_principal = round(float(args.principal))
    number_of_months = int(args.periods)
    credit_interest = float(args.interest)
    summ = 0
    if credit_principal < 0 or number_of_months < 0 or credit_interest < 0:
        print("Incorrect parameters")
        exit()
    nominal_interest_rate = (credit_interest / (12 * 100))
    for i in range(1, number_of_months + 1):
        payment = credit_principal / number_of_months + nominal_interest_rate * (credit_principal - (credit_principal * (i - 1) / number_of_months))
        print("Month " + str(i) + ": payment is " + str(math.ceil(payment)))
        summ += math.ceil(payment)
    print("Overpayment = " + str(summ - credit_principal))
if args.type == 'annuity' and args.principal and args.payment and args.interest:
    credit_principal = round(float(args.principal))
    monthly_payment = int(args.payment)
    credit_interest = float(args.interest)
    if credit_principal < 0 or monthly_payment < 0 or credit_interest < 0:
        print("Incorrect parameters")
        exit()
    nominal_interest_rate = (credit_interest / (12*100))   # calculating monthly interest rate
    logarithm_value = monthly_payment / (monthly_payment - nominal_interest_rate * credit_principal)
    number_of_months = math.ceil(math.log(logarithm_value, nominal_interest_rate + 1))  # the logarithm that counts the number of months with the 1+i base
    if monthly_payment == credit_principal:
        print("It will take 1 month to repay the credit")
    else:
        years = number_of_months // 12
        months = number_of_months % 12
        if years == 1 and months == 0:
            print("It will take " + str(years) + " year to repay this credit!")
        elif years == 1:
            print("It will take " + str(years) + " year and " + str(months) + " months to repay this credit!")
        elif months == 0:
            print("It will take " + str(years) + " years to repay this credit!")
        elif years == 0:
            print("It will take " + str(months) + " months to repay this credit!")
        else:
            print("It will take " + str(years) + " years and " + str(months) + " months to repay this credit!")
    print("Overpayment = " + str(math.ceil(monthly_payment) * number_of_months - credit_principal))
elif args.type == 'annuity' and args.principal and args.periods and args.interest:
    credit_principal = round(float(args.principal))
    number_of_months = int(args.periods)
    credit_interest = float(args.interest)
    if credit_principal < 0 or number_of_months < 0 or credit_interest < 0:
        print("Incorrect parameters")
        exit()
    nominal_interest_rate = (credit_interest / (12 * 100))
    monthly_payment = credit_principal * (nominal_interest_rate * pow(1 + nominal_interest_rate, number_of_months)) / (pow(1 + nominal_interest_rate, number_of_months) - 1)
    print("Your monthly payment = " + str(math.ceil(monthly_payment)) + '!')
    print("Overpayment = " + str(math.ceil(monthly_payment) * number_of_months - credit_principal))
elif args.type == 'annuity' and args.payment and args.periods and args.interest:
    monthly_payment = math.ceil(float(args.payment))
    number_of_months = int(args.periods)
    credit_interest = float(args.interest)
    if monthly_payment < 0 or number_of_months < 0 or credit_interest < 0:
        print("Incorrect parameters")
        exit()
    nominal_interest_rate = (credit_interest / (12 * 100))
    credit_principal = monthly_payment / ((nominal_interest_rate * pow(1 + nominal_interest_rate, number_of_months)) / (pow(1 + nominal_interest_rate, number_of_months) - 1))
    print("Your credit principal = " + str(round(credit_principal)) + "!")


