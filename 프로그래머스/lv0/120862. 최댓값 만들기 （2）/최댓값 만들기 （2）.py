def solution(numbers):
    if (sorted(numbers)[0] * sorted(numbers)[1]) >= (sorted(numbers)[-1] * sorted(numbers)[-2]):
        return sorted(numbers)[0] * sorted(numbers)[1]
    elif (sorted(numbers)[0] * sorted(numbers)[1]) < (sorted(numbers)[-1] * sorted(numbers)[-2]):
        return int(sorted(numbers)[-1] * sorted(numbers)[-2])