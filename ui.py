from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)

        self.lbl_score = Label(self.window, text="", bg=THEME_COLOR, fg="white", pady=5)
        self.lbl_score.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Text to be shown in the center",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        img_false = PhotoImage(file="images/false.png")
        self.btn_false = Button(image=img_false, highlightthickness=0, command=self.false_pressed)
        self.btn_false.grid(row=2, column=0)

        img_true = PhotoImage(file="images/true.png")
        self.btn_true = Button(image=img_true, highlightthickness=0, command=self.true_pressed)
        self.btn_true.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.lbl_score.config(text=f"Score: {self.quiz.score}")
        
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.btn_false.config(state="disabled")
            self.btn_true.config(state="disabled")

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
