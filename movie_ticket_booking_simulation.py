#  4.Movie Ticket Booking Simulation
# Simulate a movie theater booking system that:
# Shows a list of available movie titles, showtimes, and seat prices.
# Asks the user to choose a movie and number of tickets.
# Confirms total price and asks if they want to book another movie.
# Ends when they say “no” and displays total bookings and cost.
# Skills practiced: loops, input, conditionals, calculations, nested dictionaries
#Movie Title Mickey Mouse Show Time 10pm
titles= ["Mickey Mouse","Dora","Paw patrol"]
booking ={"10pm":14,
          "1pm" : 35,
          "2pm" : 45}

print("here are the available movies with their show times and seat prices!!")
index=0
booked={}
for time in booking:
    print(f"Movie Title: {titles[index]} Show Time: {time} Price: {booking.get(time)}$")
    index+=1
while True:
    title = input("pick a movie list e.g Mickey Mouse ")
    if title=="no":
        break
    if title not in titles:
        print("please enter available movie in the list only")
        continue
    num_ticket = int(input("enter the number of ticket you want to buy "))
    print("please type no when you are done!")
    ind = titles.index(title)
    show_time = list(booking.keys())[ind]
    price_per_ticket = booking[show_time]
    total_price = num_ticket * price_per_ticket
    booked[title]=total_price
print(f"The booked movie list : , {booked}")


