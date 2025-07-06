def time_to_minutes(time_str):
    hour, minute = map(int, time_str.split(":"))
    return hour * 60 + minute


def parse_train_line(line):
    parts = line.split()
    train_name = parts[0]
    departure_time = parts[-1]
    return train_name, time_to_minutes(departure_time)


def sort_trains():
    N = int(input())
    trains = []

    for index in range(N):
        line = input().strip()
        train_name, departure_minutes = parse_train_line(line)
        trains.append((train_name, -departure_minutes, index, line))

    trains.sort()
    for train in trains:
        print(train[3])

sort_trains()
