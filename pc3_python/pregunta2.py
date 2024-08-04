while True:
    try:
        grades_input = input("Enter grades separated by commas: ")
        grades_list = [int(grade.strip()) for grade in grades_input.split(',')]
        break
    except ValueError:
        print("Error: Please ensure all inputs are integers separated by commas.")

