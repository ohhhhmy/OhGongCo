h, m = map(int, input().split())

setting_m = m - 45

if setting_m < 0:
    h -= 1
    setting_m += 60

if h < 0:
    h = 23
    
print(h, setting_m)

    
