from django.shortcuts import render, HttpResponse, redirect
from .models import lcm_db
import math
from collections import Counter
from .forms import lcm_form


def lcm(request):
    # lcm_Form = lcm_form()
    try:
        if request.method == 'POST':
            form = lcm_form(request.POST)
            print("Reached in try")
            if form.is_valid()==True:

                no1 = form.cleaned_data['num1']
                no2 = form.cleaned_data['num2']
                print("Reached in try---")
                print(no1, no2)
                # no1 = int(request.POST['num1'])
                # no2 = int(request.POST['num2'])
                num1 = int(no1)
                num2 = int(no2)
                gcd = gcd_of_numbers(num1, num2)
                lcm = num1 * num2 // gcd

                # detailed function performed
                # getting all prime factors of both no's
                prime_fact_of_no1 = prime_factor(num1)
                prime_fact_of_no2 = prime_factor(num2)

                dict_of_1 = dict(Counter(prime_fact_of_no1))
                dict_of_2 = dict(Counter(prime_fact_of_no2))

                print(" Dict : ", dict_of_1)
                print(" Dict : ", dict_of_2)
                # print("set 1 :", set(dict_of_1.keys()))
                # print(" set 2 : ",set(dict_of_1.keys()))
                # po = [sorted(set(dict_of_1.keys()).union(set(dict_of_1.keys())))]
                # print(" union : all : ",po)
                result = []
                for x in sorted(set(dict_of_1.keys()).union(set(dict_of_2.keys()))):
                    print(" print union : ", x)
                    maximum_of_two = max(dict_of_1.get(x, 0), dict_of_2.get(x, 0))
                    print()
                    print(" exp : ", maximum_of_two)
                    for i in range(maximum_of_two):
                        result.append(x)

                print(result)
                # converting it to string
                prime1 = [str(i) for i in prime_fact_of_no1]
                prime2 = [str(j) for j in prime_fact_of_no2]

                # using join function to make it a single string
                prime1 = ', '.join(prime1)
                prime2 = ', '.join(prime2)
                result = " * ".join([str(i) for i in result])
                flag = True
                context = {
                    'lcm': lcm,
                    'num1': num1,
                    'num2': num2,
                    'prime1': prime1,
                    'prime2': prime2,
                    'mulresult': result,
                    'flag': flag,
                    'form':form,
                }
                # Database save
                inputEnter = str(num1) + " X " + str(num2)
                finalAnswer = lcm
                slug = '/lcm-of-{}-and-{}/'.format(num1, num2)
                solutionTitle = 'LCM of {} and {}'.format(num1, num2)

                db_details = lcm_db(inputEnter=inputEnter, detailStep=0,
                                    finalAnswer=finalAnswer, slug=slug, solutionTitle=solutionTitle)
                db_details.save()

                # return redirect('/lcm-of-{}-and-{}/'.format(no1, no2))
                return render(request, 'lcm.html', context)
        else:
            lcm_Form = lcm_form()
            flag = False
            context = {
                'flag':flag,
                'form': lcm_Form
            }
            print("Entery in get: ")
            # return render(request, 'lcm.html', context)
            return render(request, 'lcm.html', context)
    except:
        return HttpResponse("Something has failed")


def lcm_fun(request, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    gcd = gcd_of_numbers(num1, num2)
    lcm = num1*num2//gcd

    # detailed function performed
    # getting all prime factors of both no's
    prime_fact_of_no1 = prime_factor(num1)
    prime_fact_of_no2 = prime_factor(num2)

    dict_of_1 = dict(Counter(prime_fact_of_no1))
    dict_of_2 = dict(Counter(prime_fact_of_no2))

    print(" Dict : ",dict_of_1)
    print(" Dict : ", dict_of_2)
    # print("set 1 :", set(dict_of_1.keys()))
    # print(" set 2 : ",set(dict_of_1.keys()))
    # po = [sorted(set(dict_of_1.keys()).union(set(dict_of_1.keys())))]
    # print(" union : all : ",po)
    result = []
    for x in sorted(set(dict_of_1.keys()).union(set(dict_of_2.keys()))):
        print(" print union : ", x)
        maximum_of_two = max(dict_of_1.get(x,0), dict_of_2.get(x,0))
        print()
        print(" exp : ", maximum_of_two)
        for i in range(maximum_of_two):
            result.append(x)

    print(result)
    # converting it to string
    prime1 = [str(i) for i in prime_fact_of_no1]
    prime2 = [str(j) for j in prime_fact_of_no2]

    # using join function to make it a single string
    prime1 = ', '.join(prime1)
    prime2 = ', '.join(prime2)
    result = " * ".join([str(i) for i in result])

    context = {
        'lcm': lcm,
        'num1': num1,
        'num2': num2,
        'prime1': prime1,
        'prime2': prime2,
        'mulresult':result
    }
    #Database save
    inputEnter = str(num1)+" X "+str(num2)
    finalAnswer = lcm
    slug = '/lcm-of-{}-and-{}/'.format(num1, num2)
    solutionTitle = 'LCM of {} and {}'.format(num1, num2)

    db_details = lcm_db(inputEnter=inputEnter, detailStep= 0,
                        finalAnswer = finalAnswer, slug=slug, solutionTitle=solutionTitle)
    db_details.save()

    return render(request, 'lcm_fun.html', context)

def calculator(request):
    return HttpResponse("Calculat page")

# function for finding LCM using gcd:
def gcd_of_numbers(no1, no2):
    divisor = no1
    divident = no2
    print(" no in gdc ")
    print(divisor, divident)
    rem = divident%divisor
    while rem != 0:
        divident = divisor
        divisor = rem
        rem = divident%divisor
    print(divisor)
    return divisor

# function to find prime factor and return list
def prime_factor(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n = n//i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# def prime_factor(no):
#     result = []
#     for i in range(2,no+1):
#         if no%i == 0:
#             j = 2
#             isprime = 1
#             while j*j <= i:
#                 if i%j==0:
#                     isprime = 0
#                     break
#                 j+=1
#             if isprime == 1:
#                 result.append(i)
#     return result



