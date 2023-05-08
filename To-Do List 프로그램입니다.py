#To-Do List 프로그램입니다

tasks = []

def add_task():
    task = input("추가할 일을 입력하세요: ")
    tasks.append(task)
    print("일이 추가되었습니다.")

def delete_task():
    task_num = int(input("삭제할 일의 번호를 입력하세요: "))
    if task_num < 1 or task_num > len(tasks):
        print("잘못된 번호입니다.")
    else:
        del tasks[task_num-1]
        print("일이 삭제되었습니다.")

def view_tasks():
    if not tasks:
        print("할 일이 없습니다.")
    else:
        print("할 일 목록:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

while True:
    print("="*30)
    print("1. 일 추가")
    print("2. 일 삭제")
    print("3. 일 목록 보기")
    print("4. 종료")
    choice = input("원하는 작업을 선택하세요: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 선택해주세요.")