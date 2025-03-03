sec= int(input("Введіть секунди: "))

if 0 <= sec < 8640000 :
    day, sec = divmod(sec, 86400)
    hour, sec = divmod(sec, 3600)
    min, sec = divmod(sec, 60)

    a= "day" if day == 1 else "days" if 2 <= day <= 4 else "days"

    print(f"{day} {a}, {str(hour). zfill(2)} : {str(min). zfill(2)}:{str(sec). zfill(2)}")
else :
    print("Число повинно бути від 0 до 8640000")