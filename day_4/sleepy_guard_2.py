from datetime import datetime

def main():
    chronological_order = []
    aggregate_time_asleep = []

    # Parsing input file
    with open('input.txt') as input_file:
        for line in input_file:
            date = line[:18]
            content = line[18:]
            year = int(date[1:5])
            month = int(date[6:8])
            day = int(date[9:11])
            hour = int(date[12:14])
            minute = int(date[15:17])
            dt = datetime(year, month, day, hour, minute)
            chronological_order.append((dt, content))

    # Sorting all entries in chronological order
    chronological_order = sorted(chronological_order, key=lambda x: x[0])

    skip = True
    fell_asleep = None
    time_asleep = None
    current_guard = None

    # Finding sleep time for each guard entry
    for entry in chronological_order:
        if(entry[1].strip() == 'falls asleep'):
            fell_asleep = entry[0]
        if(entry[1].strip() == 'wakes up'):
            minutes_elapsed = str((entry[0] - fell_asleep)).split(':')[1]
            time_asleep += int(minutes_elapsed)
        if(entry[1].strip()[:5] == 'Guard'):
            if(not skip):
                aggregate_time_asleep.append((current_guard, time_asleep))
            tmp = entry[1].split('#')
            tmp = tmp[1].split(' ')
            current_guard = tmp[0]
            skip = False
            time_asleep = 0

    # Sorting aggregated sleep to group the guards together
    aggregate_time_asleep = sorted(aggregate_time_asleep, key=lambda x: x[0])

    current_guard = aggregate_time_asleep[0][0]
    sleep_time = 0

    aggregate_sleep_time_by_elf = []

    # Aggregating sleep times by elf
    for sleep_entry in aggregate_time_asleep:
        if(sleep_entry[0] == current_guard):
            sleep_time += sleep_entry[1]
        else:
            aggregate_sleep_time_by_elf.append((current_guard, sleep_time))
            current_guard = sleep_entry[0]
            sleep_time = sleep_entry[1]

    # Sorting by aggregate sleep time to find the sleepiest elf
    aggregate_sleep_time_by_elf = sorted(aggregate_sleep_time_by_elf, key=lambda x: x[1])
    # THE SLEEPIEST ELF
    sleepiest_elf = aggregate_sleep_time_by_elf[len(aggregate_sleep_time_by_elf) - 1]

    current_guard2 = None
    fell_asleep2 = None
    time_awoken = None

    times_asleep_minute_array = [0 for x in range(60)]

    for entry in chronological_order:
        if(entry[1].strip()[:5] == 'Guard'):
            tmp = entry[1].split('#')
            tmp = tmp[1].split(' ')
            current_guard2 = tmp[0]
        if (current_guard2 == sleepiest_elf[0]):
            if(entry[1].strip() == 'falls asleep'):
                fell_asleep2 = entry[0]
            if(entry[1].strip() == 'wakes up'):
                time_awoken = entry[0]
                fell_asleep_min = str(fell_asleep2).split(':')[1]
                time_awoken_min = str(time_awoken).split(':')[1]
                for x in range(int(fell_asleep_min), int(time_awoken_min)):
                    times_asleep_minute_array[x] = times_asleep_minute_array[x] + 1

    print(times_asleep_minute_array)
    print(times_asleep_minute_array.index(15))
    print(sleepiest_elf[0])

if __name__ == "__main__":
    main()