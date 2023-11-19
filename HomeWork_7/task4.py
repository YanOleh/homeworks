days_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dict1 = {i+1: day for i, day in enumerate(days_week)}
dict2 = {days_week[i]: i +1 for i in range(len(days_week))}

print(dict1)
print(dict2)