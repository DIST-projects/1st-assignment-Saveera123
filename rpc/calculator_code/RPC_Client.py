import xmlrpc.client

# Connect to RPC server
server = xmlrpc.client.ServerProxy("http://13.60.215.102:8000", allow_none=True)
print("Connected to RPC Server")

while True:
    print("\n--- RPC Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting program...")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result (Add):", server.add(a, b))

    elif choice == 2:
        print("Result (Subtract):", server.subtract(a, b))

    elif choice == 3:
        print("Result (Multiply):", server.multiply(a, b))

    elif choice == 4:
        print("Result (Divide):", server.divide(a, b))

    else:
        print("Invalid choice! Please try again.")