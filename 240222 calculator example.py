import tkinter as tk

def create_app():
    # 기본 윈도우 생성
    window = tk.Tk()
    window.title("계산기")

    # 입력 필드 생성
    entry = tk.Entry(window, width=40, borderwidth=5)
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    #버튼 추가 함수
    def add_button(text, row, column, command=None):
        button = tk.Button(window, text=text, padx=40, pady=20, command=command)
        button.grid(row=row, column=column)
    
    #숫자 버튼 생성
    numbers = [str(i) for i in range(1,10)] + ["0"]
    positions = [(i // 3 + 1, i % 3) for i in range(9)] + [(4,1)]
    for number, pos in zip(numbers, positions):
        add_button(number, pos[0], pos[1])

    # 연산자 버튼 생성
    add_button("+", 1, 3)
    add_button("-", 2, 3)
    add_button("*", 3, 3)
    add_button("/", 4, 3)

    window.mainloop()

create_app()

current_expression = ""

def append_to_expression(text):
    global current_expression
    current_expression += str(text)
    entry.delete(0, tk.END)
    entry.insert(0, current_expression)

def calculate_expression():
    global current_expression
    try:
        result = eval(current_expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        current_expression = str(result)
    except:
        clear.entry()
        entry.insert(0, "Error")

def clear_entry():
    global current_expression
    current_expression = ""
    entry.delete(0, tk.END)

#숫자 버튼 업데이트
    
for number, pos in zip(numbers, positions):
    add_button(number, pos[0], pos[1], lambda n=number: append_to_expression(n))

# 연산자 버튼 및 기능 버튼 추가
add_button("+", 1, 3, lambda: append_to_expression("+"))
add_button("-", 2, 3, lambda: append_to_expression("-"))
add_button("*", 3, 3, lambda: append_to_expression("*"))
add_button("/", 4, 3, lambda: append_to_expression("/"))
add_button("=", 4, 2, calculate_expression)
add_button("C", 4, 0, clear_entry)
