def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    result = 0

    for x in permanence_period:
        if type(x[0]) != int or type(x[1]) != int:
            return None
        if int(x[0]) <= target_time <= int(x[1]):
            result += 1
    return result
# fim
