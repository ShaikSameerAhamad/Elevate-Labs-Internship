def add(a,b):
	return a+b
def sub(a,b):
	return a-b 
def mul(a,b):
	return a*b
def div(a,b):
	return float(a/b)
def mod(a,b):
	return float(a%b)  
def main():
	while True:
		print("\nEnter two numbers:")
		a = int(input("Enter a: "))
		b = int(input("Enter b: "))
		print("Choose the operation to perform:")
		print("+ for Addition")
		print("- for Subtraction")
		print("* for Multiplication")
		print("/ for Division")
		print("% for Modulus")
		print("Type 'exit' to quit")
		op = input("Enter operation (+, -, *, /, %, exit): ").strip()
		if op == '+':
			print(f"Result: {add(a, b)}")
		elif op == '-':
			print(f"Result: {sub(a, b)}")
		elif op == '*':
			print(f"Result: {mul(a, b)}")
		elif op == '/':
			if b == 0:
				print("Error: Division by zero!")
			else:
				print(f"Result: {div(a, b)}")
		elif op == '%':
			if b == 0:
				print("Error: Modulus by zero!")
			else:
				print(f"Result: {mod(a, b)}")
		elif op.lower() == 'exit':
			print("Exiting calculator. Goodbye!")
			break
		else:
			print("Invalid operation. Please try again.")

if __name__ == "__main__":
	main()

