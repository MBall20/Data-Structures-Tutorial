class Escalator:
    def __init__(self, max_size):
        self.queue = []
        if max_size <= 0:
            self.max_size = 10  # Default value if max size is invalid
        else:
            self.max_size = max_size

    def add_new_customer(self):
        if len(self.queue) >= self.max_size:
            print("Maximum Number of Customers on the Escalator.")
            return

        name = input("Customer Name: ")
        self.queue.append(name)

    def serve_customer(self):
        # Need to check to make sure there are customers in the queue
        if len(self.queue) == 0:     
            print("No Customers in the Escalator")
        else:
            # Need to read and save the customer before it is deleted from the queue
            customer = self.queue[0]
            del self.queue[0] 
            # print customer removed from queue        
            print(f"{customer} got off the escalator")

    def __str__(self):
        """ 
        Display the people on the escalator without square brackets and qotation marks
        """
        
        return "Customers on the escalator: " + str(self.queue).strip('[]').replace("'", "")


# test case 1: 5 people get on the escalator
print("\nTest 1")
escalator = Escalator(10)
for i in range(5):
    escalator.add_new_customer()
print(escalator)


# test case 2: 2 people get off the escalator
print("\nTest 2")
for i in range(2):
    escalator.serve_customer()
print(escalator)

# test case 3: 8 people get on the escalator
print("\nTest 3")
for i in range(8):
    escalator.add_new_customer()
print(escalator)

# test case 4: 2 people get off the escalator
print("\nTest 4")
for i in range(2):
    escalator.serve_customer()
print(escalator)

# test case 5: 8 people get off the escalator
print("\nTest 5")
for i in range(8):
    escalator.serve_customer()
print(escalator)

# test case 6: 1 person gets off the escalator
print("\nTest 6")
escalator.serve_customer()

