 def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total

tom_exp_list=[2100,3400,3500]
joe_exp_list=[200,500,700]
toms_total=calculate_total(tom_exp_list)
joe_total=calculate_total(joe_exp_list)

print("Tom's total expenses:",toms_total)
print("Joe's total expense:", joe_total)