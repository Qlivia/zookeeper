HOURS_MULTIPLIER = 3600
MINUTES_MULTIPLIER = 60

walk_hour = abs(int(input()))
walk_minutes = abs(int(input()))
walk_seconds = abs(int(input()))

walk_time = (walk_hour * HOURS_MULTIPLIER) + (walk_minutes * MINUTES_MULTIPLIER) + walk_seconds

rain_hour = abs(int(input()))
rain_minutes = abs(int(input()))
rain_seconds = abs(int(input()))

rain_time = (rain_hour * HOURS_MULTIPLIER) + (rain_minutes * MINUTES_MULTIPLIER) + rain_seconds

print(rain_time - walk_time)
