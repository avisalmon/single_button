import tkinter as tk

class PongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="black")
        self.canvas.pack()

        self.ball = self.canvas.create_oval(290, 190, 310, 210, fill="white")
        self.left_paddle = self.canvas.create_rectangle(20, 150, 30, 250, fill="white")
        self.right_paddle = self.canvas.create_rectangle(570, 150, 580, 250, fill="white")

        self.ball_speed_x = 3
        self.ball_speed_y = 3
        self.paddle_speed = 20

        self.root.bind("<KeyPress-w>", lambda _: self.move_paddle(self.left_paddle, -self.paddle_speed))
        self.root.bind("<KeyPress-s>", lambda _: self.move_paddle(self.left_paddle, self.paddle_speed))
        self.root.bind("<KeyPress-Up>", lambda _: self.move_paddle(self.right_paddle, -self.paddle_speed))
        self.root.bind("<KeyPress-Down>", lambda _: self.move_paddle(self.right_paddle, self.paddle_speed))

        self.update_game()

    def move_paddle(self, paddle, dy):
        self.canvas.move(paddle, 0, dy)
        self.canvas.update()

    def update_game(self):
        self.move_ball()
        self.check_collision()
        self.root.after(30, self.update_game)

    def move_ball(self):
        self.canvas.move(self.ball, self.ball_speed_x, self.ball_speed_y)
        self.canvas.update()

    def check_collision(self):
        x1, y1, x2, y2 = self.canvas.coords(self.ball)

        if x1 <= 0 or x2 >= 600:
            self.ball_speed_x *= -1
        if y1 <= 0 or y2 >= 400:
            self.ball_speed_y *= -1

        if self.collides_with_paddle(self.left_paddle) or self.collides_with_paddle(self.right_paddle):
            self.ball_speed_x *= -1

    def collides_with_paddle(self, paddle):
        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(paddle)
        overlap = self.canvas.find_overlapping(*ball_coords)
        return paddle in overlap

root = tk.Tk()
game = PongGame(root)
root.mainloop()
