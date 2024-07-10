class RestaurantQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Order '{order}' has been added to the queue.")

    def dequeue(self):
        if len(self.queue) > 0:
            order = self.queue.pop(0)
            print(f"Order '{order}' has been served.")
            return order
        else:
            print("No orders in the queue to serve.")
            return None

    def display_queue(self):
        if len(self.queue) > 0:
            print("Current queue:", self.queue)
        else:
            print("The queue is empty.")

if __name__ == "__main__":
    restaurant_queue = RestaurantQueue()

    while True:
        print("\nRestaurant Order Queue System")
        print("1. Add order (Enqueue)")
        print("2. Serve order (Dequeue)")
        print("3. Display current queue")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            order = input("Enter the order to add: ")
            restaurant_queue.enqueue(order)
        elif choice == '2':
            restaurant_queue.dequeue()
        elif choice == '3':
            restaurant_queue.display_queue()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")