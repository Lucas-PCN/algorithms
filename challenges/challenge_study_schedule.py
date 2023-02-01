def study_schedule(permanence_period, target_time):
    try:
        students_studying = 0

        for start, end in permanence_period:
            if start <= target_time <= end:
                students_studying += 1

        return students_studying

    except TypeError:
        return None
