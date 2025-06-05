import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x500")
        self.root.resizable(False, False)

        self.expression = ""
        self.last_successful_expression = ""  # 마지막 정상 계산된 식

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 레이아웃
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['Undo', '=', '되돌리기']  # 복원 버튼 추가
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == 'Undo':
            # 마지막 한 글자 삭제
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                result = eval(self.expression)
                self.last_successful_expression = self.expression  # 계산 성공 시 저장
                self.expression = str(round(result, 10))
            except Exception:
                self.expression = "에러"
        elif char == '되돌리기':
            # 마지막 성공한 식으로 복원
            if self.last_successful_expression:
                self.expression = self.last_successful_expression
        else:
            self.expression += str(char)

        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
