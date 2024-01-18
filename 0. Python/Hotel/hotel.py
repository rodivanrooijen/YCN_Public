from diagrams import Diagram, Cluster
from diagrams.custom import Custom

# Create a class diagram for the hotel booking system
with Diagram("Hotel Booking System Class Diagram", show=False, direction="TB"):
    # Defining the classes
    hotel = Custom("Hotel", "./resources/hotel.png")
    room = Custom("Room", "./resources/room.png")
    reservation = Custom("Reservation", "./resources/reservation.png")
    customer = Custom("Customer", "./resources/customer.png")
    account = Custom("Account", "./resources/account.png")
    payment_method = Custom("Payment Method", "./resources/payment.png")
    loyalty_program = Custom("Loyalty Program", "./resources/loyalty.png")

    # Defining relationships
    hotel - room
    customer - reservation
    reservation - room
    account - customer
    reservation - payment_method
    customer - loyalty_program
    account - reservation

# Note: This diagram is a high-level representation and might not include all necessary details for implementation. 
# It's meant to provide a conceptual understanding of the main components and their relationships.
