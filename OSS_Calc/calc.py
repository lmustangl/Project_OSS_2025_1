import tkinter as tk

EXCHANGE_RATE = 1380  # 1 USD = 1380 KRW

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""
        self.krw_mode = True  # True: KRW → USD, False: USD → KRW

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 배열
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['환율변환', '=']
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
            self.krw_mode = True  # 원화 기준으로 초기화
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == '환율변환':
            try:
                # 숫자만 남기고 단위 제거
                clean_expr = ''.join(filter(lambda c: c.isdigit() or c == '.' or c == '-', self.expression))
                amount = float(clean_expr)

                if self.krw_mode:
                    result = amount / EXCHANGE_RATE
                    self.expression = str(round(result, 4))
                else:
                    result = amount * EXCHANGE_RATE
                    self.expression = str(round(result, 2))

                self.krw_mode = not self.krw_mode  # 모드 전환
            except Exception:
                self.expression = "환율 오류"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

# 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
