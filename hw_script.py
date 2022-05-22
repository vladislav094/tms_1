def check_type():
    while True:
        func = input(f"Please, type letter / digital / spec.character: ")
        if func == 'x':
            break
        elif func.isdigit():
            print('Is digit', func)
        elif func.isalpha() == False and func.isdigit() == False:
            print(f"Spec.character")
        elif func.isupper() == True:
            print(f"letter is upper")
        elif func.islower() == True:
            print(f"Letter is lower")

# check_type()

def who_beautiful():
    v_1 = "вроде Я"
    v_2 = "точно Я"
    v_3 = "Пока не поняла"
    answer = "На свете всех милее "
    question = input(f"Кто на свете всех милее?:\n{v_1} - 1,\n{v_2} - 2,\n{v_3} - 3 \nВаш ответ: ").lower()
    if question == v_1.lower():
        print(f"{answer}{v_1}")
    if question == v_2.lower():
        print(f"{answer}{v_2}")
    else:
        print(f"Так определяйся быстрее!!!")

who_beautiful()
