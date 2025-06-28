# 4: Movie Ticket Booking Simulation
#python_project_movie_ticket_booking_simulation_batch13_group3
# Steps to follow:
    # 1: Define a dictionary of movies with showtime and price
    # 2: Track total tickets and total cost
    # 3: Display movie list to user
    # 4: Loop for booking
    # 5: Display User Instructions
    # 6: Ask how many tickets and calculate cost
    # 7: Show booking summary
# Step 1: Define a dictionary of movies with showtime and price
movies = {
    "Freedom Writers": {"time": "7:00 PM", "price": 10.0},
    "The Notebook": {"time": "5:30 PM", "price": 10.5},
    "The Pursuit of Happyness": {"time": "9:00 PM", "price": 12.0}
}

# Step 2: Track total tickets, total cost, and individual bookings
total_tickets = 0
total_cost = 0
bookings = {}  # Dictionary to store bookings: {movie: tickets}

# Step 3: Display movie list to user
print("Welcome to Group 3 Cinema Movie Booking System!")
print("\nAvailable Movies")
print("============================================================")
for title, info in movies.items():
    print(f"{title} - {info['time']} - ${info['price']:.2f} per ticket")

# Step 4: Display User Instructions
print("\nUser Instruction: Please make sure to follow the steps below")
print("============================================================")
print("1. First enter the title of the available movie")
print("2. Enter the number of required tickets")
print("3. Enter 'done' to finish")

# Step 5: Loop for booking
while True:
    choice = input("\nEnter movie name to book or type 'done' to finish: ").strip()
    if choice.lower() == "done":
        break
    if choice not in movies:
        print("Sorry, the requested movie is not currently available. Try again.")
        continue
    try:
        # Step 6: Ask how many tickets and calculate cost
        tickets = int(input("How many tickets? "))
        if tickets <= 0:
            raise ValueError
        cost = tickets * movies[choice]["price"]
        total_tickets += tickets
        total_cost += cost
        # Store booking details
        if choice in bookings:
            bookings[choice] += tickets
        else:
            bookings[choice] = tickets
    except ValueError:
        print("Please enter a valid number of tickets.")

# Step 7: Show booking summary
if bookings:
    print("\nBooking Summary")
    print("============================================================")
    for movie, tickets in bookings.items():
        cost = tickets * movies[movie]["price"]
        print(f"Booked {tickets} ticket(s) for '{movie}' - Total: ${cost:.2f}")
    print(f"\nTotal tickets booked: {total_tickets}")
    print(f"Total cost: ${total_cost:.2f}")
else:
    print("\nNo bookings made.")