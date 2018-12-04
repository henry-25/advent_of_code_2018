from datetime import datetime

def main():
    chronological_order = []
    # Dict with elf id as key and array with hours slept in as value
    times_asleep_by_elf = {}

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

    fell_asleep = None
    time_awoken = None
    current_guard = None

    for entry in chronological_order:
        if(entry[1].strip()[:5] == 'Guard'):
            print(entry[1])
            tmp = entry[1].split('#')
            tmp = tmp[1].split(' ')
            current_guard = tmp[0]
            print(current_guard)
        if(entry[1].strip() == 'falls asleep'):
            fell_asleep = str(entry[0]).split(':')[1]
        if(entry[1].strip() == 'wakes up'):
            time_awoken = str(entry[0]).split(':')[1]
            if(current_guard in times_asleep_by_elf):
                for x in range(int(fell_asleep), int(time_awoken)):
                    times_asleep_by_elf[current_guard][x] += 1
            else:
                times_asleep_minute_array = [0 for x in range(60)]
                times_asleep_by_elf[current_guard] = times_asleep_minute_array
                for x in range(int(fell_asleep), int(time_awoken)):
                    times_asleep_by_elf[current_guard][x] += 1
    
    print(times_asleep_by_elf)

    highest_freq_id = 0
    highest_freq_time = 0
    highest_freq_value = 0

    for key in times_asleep_by_elf:
        for x in range(60):
            if(times_asleep_by_elf[key][x] > highest_freq_value):
                highest_freq_id = key
                highest_freq_time = x
                highest_freq_value = times_asleep_by_elf[key][x]
                print(highest_freq_id, highest_freq_time, highest_freq_value)

    print(times_asleep_by_elf['1657'])

        #     minutes_elapsed = str((entry[0] - fell_asleep)).split(':')[1]
        #     time_asleep += int(minutes_elapsed)
        # if(entry[1].strip()[:5] == 'Guard'):
        #     if(not skip):
        #         aggregate_time_asleep.append((current_guard, time_asleep))
        #     tmp = entry[1].split('#')
        #     tmp = tmp[1].split(' ')
        #     current_guard = tmp[0]
        #     skip = False
        #     time_asleep = 0

if __name__ == "__main__":
    main()