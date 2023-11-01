c = input("Letter (a-z): ")
c = c.lower() # Преобразование введенного символа в нижний регистр, чтобы учесть разные регистры
letter_number = ord(c) - ord('a') + 1
print(f"Номер буквы {c} в алфавите: {letter_number}")