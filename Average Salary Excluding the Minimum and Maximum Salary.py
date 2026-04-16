def averageSalary(salary):

    min_val = float('inf')
    max_val = float('-inf')
    total_sum = 0

    for i in range(len(salary)):
        total_sum += salary[i]

        if salary[i] < min_val:
            min_val = salary[i]

        if salary[i] > max_val:
            max_val = salary[i]

    adjusted_sum = total_sum - min_val - max_val

    result = adjusted_sum/(len(salary) - 2)

    return result

print(averageSalary([4000,3000,1000,2000]))