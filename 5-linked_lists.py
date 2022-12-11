'''

'''
# Create a Route class
class Route:

    # Create a Stop class
    class Stop:
        '''
        Each stop will be connected to the stop before and after it.
        '''
        def __init__(self, destination):
            '''
            Initialize the  stop to the data provided.
            '''
            self.destination = destination
            self.next = None
            self.prev = None

    def __init__(self):
        '''
        Initialize an empty Route
        '''
        self.head = None
        self.tail = None

    
    def add_beginning(self, destination):
        '''
        Add a stop to the beginning of the route
        '''
        # Create the new stop
        new_stop = Route.Stop(destination)

        # If the stop is empty, then point both head and tail to the new stop
        if self.head is None:
            self.head = new_stop
            self.tail = new_stop
        # If the route is not empty, then only self.head will be affected
        else:
            new_stop.next = self.head
            self.head.prev = new_stop
            self.head = new_stop

    def add_end(self, destination):
        '''
        Add a stop to the end of the route
        '''
        # Create the new stop
        new_stop = Route.Stop(destination)

        # Empty route
        if self.head is None:
            self.head = new_stop
            self.tail = new_stop
        
        # Route is not empty
        else:
            self.tail.next = new_stop
            new_stop.prev = self.tail
            self.tail = new_stop

    def remove_beginning(self):
        '''
        Remove the first stop from the route
        '''
        # Only one stop on the route
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # More than one stop on the route
        else:
            # Remove the first stop from the route
            self.head.prev = None
            self.head = self.head.next
            
    def remove_end(self):
        '''
        Remove the last stop from the route
        '''
        # Only one stop on the route
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # More than one stop on the route
        else:
            # Remove the last stop from the route
            self.tail.prev.next = None
            self.tail = self.tail.prev

    # add a stop after a specific stop
    def new_stop(self, destination, new_destination):
        '''
        Add a new stop after the specified destination
        '''
        # Find the stop on the route that matches the destination
        current_stop = self.head
        while current_stop is not None:
            if current_stop.destination == destination:

                if current_stop == self.tail:
                    self.add_end(new_destination)
                
                else:
                    new_stop = Route.Stop(new_destination)
                    new_stop.prev = current_stop
                    new_stop.next = current_stop.next
                    current_stop.next = new_stop

            # Move to the next stop in line
            current_stop = current_stop.next

    def remove_stop(self, destination):
        '''
        Remove a stop from the route
        '''
        # Find the stop on the route that matches the destination
        current_stop = self.head
        while current_stop is not None:
            if current_stop.destination == destination:

                if current_stop == self.head:
                    self.remove_beginning()
                
                elif current_stop == self.tail:
                    self.remove_end()

                else:
                    current_stop.prev.next = current_stop.next
                    current_stop.next.prev = current_stop.prev

            # Move to the next stop in line
            current_stop = current_stop.next

    def __iter__(self):
        """
        Iterate over the route.
        """
        current = self.head
        while current is not None:
            yield current.destination
            current = current.next
    
    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "Route: "
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        
        return output

# Sample Test
route = Route()
# Test 1
print("Test 1: Initial route")
route.add_beginning("Stop 1")
route.add_end("Stop 2")
route.add_end("Stop 3")
route.add_end("Stop 4")
print(route)

# Test 2
print()
print("Test 2: Add a stop in the middle")
route.new_stop("Stop 2", "Stop 2.5")
print(route)

# Test 3
print()
print("Test 3: Remove a stop in the middle")
route.remove_stop("Stop 2")
print(route)

# Test 4
print()
print("Test 4: Remove the first stop")
route.remove_beginning()
print(route)

# Test 5
print()
print("Test 5: Remove the last stop")
route.remove_end()
print(route)

