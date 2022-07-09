times_rode = int(input("How many times have you rode the bus last month?: "))
cost = float(input("How much does it cost for one bus ride?: "))
total_cost = times_rode * cost
print("You have ridden the bus " + str('{:.2f}'.format(times_rode)) + " times. One bus ride costs $" + str('{:.2f}'.format(cost)) + ". Your total cost was $" + str('{:.2f}'.format(total_cost)) + '.')

