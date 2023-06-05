def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for x, j in permanence_period:
        if not all(isinstance(value, int) for value in (x, j)) or x is None or j is None:
            return None
        if x <= target_time <= j:
            count += 1
    return count
