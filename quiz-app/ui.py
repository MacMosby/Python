from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.scoreboard = Label(text=f"Score: {self.score}", bg=THEME_COLOR)
        self.scoreboard.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )

        yes_img = PhotoImage(file="images/true.png")
        self.yes = Button(image=yes_img, highlightthickness=0, command=self.true_pressed)
        self.yes.grid(column=0, row=2)

        no_img = PhotoImage(file="images/false.png")
        self.no = Button(image=no_img, highlightthickness=0, command=self.false_pressed)
        self.no.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz. Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.yes.config(state="disabled")
            self.no.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
