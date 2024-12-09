from datetime import datetime, timedelta

def calculate_future_date():
    while True:
        try:
            days = int(input("Количество дней: "))
            break
        except ValueError:
            print("Ошибка: введите целое число.")
    
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    
    print(f"Дата через {days} дней: {future_date.strftime('%d-%m-%Y')}")
calculate_future_date()