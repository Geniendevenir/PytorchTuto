class Square:
	def __init__(self, w, h):
		self.width = w
		self.heigth = h
		self.color = "red"
	
	def print_info(self, name="Square"):
		print(f"{name} with width: {self.width}, height: {self.heigth}, color: {self.color}")

class Rectangle(Square):
	def __init__(self, w, h):
		super().__init__(w, h)
		super().print_info("Rectangle")
		self.color = "blue"
		super().print_info("Rectangle after color change")

if __name__ == "__main__":
	rect = Rectangle(10, 20)

