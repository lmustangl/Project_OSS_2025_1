from budget import Budget

def main():
    budget = Budget()

    while True:
        print("=== 가계부 프로그램 ===")
        print("1. 지출 추가")
        print("2. 수익 추가")
        print("3. 지출 목록 보기")
        print("4. 수익 목록 보기")
        print("5. 총 지출 보기")
        print("6. 총 수익 보기")
        print("7. 순이익 보기")
        print("0. 종료")
        choice = input("원하는 작업을 선택하세요: ")

        if choice == "1":
            category = input("지출 카테고리: ")
            description = input("지출 설명: ")
            amount = int(input("지출 금액: "))
            budget.add_expense(category, description, amount)

        elif choice == "2":
            description = input("수익 설명: ")
            amount = int(input("수익 금액: "))
            budget.add_income(description, amount)

        elif choice == "3":
            budget.list_expenses()

        elif choice == "4":
            budget.list_incomes()

        elif choice == "5":
            budget.total_spent()

        elif choice == "6":
            budget.total_income()

        elif choice == "7":
            budget.net_income()

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 시도해 주세요.\n")

if __name__ == "__main__":
    main()
