days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def add_time(start, duration, start_day=None):
    initial_hours = int(start.split(' ')[0].split(':')[0])
    initial_minutes = int(start.split(' ')[0].split(':')[1])
    suffix = start.split(' ')[1]

    hours_to_add = int(duration.split(":")[0])
    minutes_to_add = int(duration.split(":")[1])

    total_minutes = initial_minutes + minutes_to_add
    wrap_hour, new_minutes = divmod(total_minutes, 60)
    total_hours = initial_hours + wrap_hour + hours_to_add
    wrap_day, new_hours = divmod(total_hours, 24)
    
    if len(str(new_minutes)) == 1:
        new_minutes = f'0{new_minutes}'
        
    #print(wrap_day, total_hours, new_hours)   
    if suffix == 'AM':  
        if new_hours == 12:
            suffix = 'PM'
        elif new_hours > 12:
            new_hours -= 12
            suffix = 'PM'
        elif wrap_day == 1:
            suffix = 'AM (next day)'
    elif suffix == 'PM':
        if new_hours == 12:
            suffix = 'AM'
        elif new_hours > 12:
            new_hours -= 12
            suffix = 'AM (next day)'
        elif wrap_day == 1:
            suffix = 'AM'
    
    if start_day:
        start_day = start_day.title()
        if wrap_day != 0:
            index = days.index(start_day)
            wrap_index = (index + total_hours%7 + 1)%7
            new_day = days[wrap_index]
        else:
            new_day = f', {start_day}'


    if start_day:
        if wrap_day != 0:
            new_time = ':'.join([str(new_hours), str(new_minutes)]) + f' {suffix}, ' + new_day + f' ({wrap_day+1} days later)'
        else:
            new_time = ':'.join([str(new_hours), str(new_minutes)]) + f' {suffix}' + new_day
    else:
        if hours_to_add == 24:
            new_time = ':'.join([str(new_hours), str(new_minutes)]) + f' {suffix}'
        elif wrap_day != 0:
            new_time = ':'.join([str(new_hours), str(new_minutes)]) + f' {suffix}' + f' ({wrap_day+1} days later)'
        else:
            new_time = ':'.join([str(new_hours), str(new_minutes)]) + f' {suffix}'

    
    print(new_time)

add_time("11:59 PM", "24:05")

'''  

    def test_two_days_later(self):
        actual = add_time("11:59 PM", "24:05")
        expected = "12:04 AM (2 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05" to return "12:04 AM (2 days later)"')

    def test_high_duration(self):
        actual = add_time("8:16 PM", "466:02")
        expected = "6:18 AM (20 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02" to return "6:18 AM (20 days later)"')

    def test_no_change(self):
        actual = add_time("5:01 AM", "0:00")
        expected = "5:01 AM"
        self.assertEqual(actual, expected, 'Expected adding 0:00 to return initial time.')

    def test_same_period_with_day(self):
        actual = add_time("3:30 PM", "2:12", "Monday")
        expected = "5:42 PM, Monday"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12", "Monday" to return "5:42 PM, Monday"')

    def test_twenty_four_with_day(self):
        actual = add_time("2:59 AM", "24:00", "saturDay")
        expected = "2:59 AM, Sunday (next day)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00", "saturDay" to return "2:59 AM, Sunday (next day)"')

    def test_two_days_later_with_day(self):
        actual = add_time("11:59 PM", "24:05", "Wednesday")
        expected = "12:04 AM, Friday (2 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05", "Wednesday" to return "12:04 AM, Friday (2 days later)"')

    def test_high_duration_with_day(self):
        actual = add_time("8:16 PM", "466:02", "tuesday")
        expected = "6:18 AM, Monday (20 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02", "tuesday" to return "6:18 AM, Monday (20 days later)"')'''