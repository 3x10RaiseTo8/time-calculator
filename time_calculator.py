def add_time(start, duration, day=None):

    # Defining given variables
    start_hour = int(start.split(':')[0])
    start_minute = int(start.split()[0].split(':')[1])
    day_section = start.split()[1]
    day = day.capitalize() if day else None
    add_hour = int(duration.split(':')[0])
    add_minute = int(duration.split(':')[1])
    day_counter = 0
    note = None
    day_list = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Adding Hours
    final_hour = start_hour + add_hour

    while final_hour > 12:
        final_hour = final_hour - 12
        if day_section == 'AM':
            day_section = 'PM'
        else:
            day_section = 'AM'
            day_counter += 1

            if day:
                dayindex = day_list.index(day)
                try:
                    day = day_list[dayindex + 1]
                except:
                    day = day_list[0]

    # Adding Minutes
    final_minute = start_minute + add_minute

    if final_minute > 60:
        final_minute = final_minute - 60
        if final_hour == 11 and day_section == 'AM':
            day_section = 'PM'
        elif final_hour == 11 and day_section == 'PM':
            day_section = 'AM'
            day_counter += 1
            if day != None:
                dayindex = day_list.index(day)
                try:
                    day = day_list[dayindex + 1]
                except:
                    day = day_list[0]
        final_hour += 1
    if len(str(final_minute)) == 1:
        final_minute = '0' + str(final_minute)

    # Note if the date changes
    if day_counter == 1:
        note = '(next day)'
    elif day_counter > 1:
        note = f'({str(day_counter)} days later)'

    # Resultant Time
    time = f"{final_hour}:{final_minute} {day_section}"

    if day:
        if note:
            return f"{time}, {day} {note}"
        else:
            return f"{time}, {day}"
    else:
        if note:
            return f"{time} {note}"
    return time
