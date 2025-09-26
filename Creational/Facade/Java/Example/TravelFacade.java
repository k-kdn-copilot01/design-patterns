package Creational.Facade.Java.Example;

public class TravelFacade {
    private final FlightBooking flight = new FlightBooking();
    private final HotelBooking hotel = new HotelBooking();
    private final PaymentGateway payment = new PaymentGateway();

    public String bookTrip(String name) {
        String f = flight.book(name);
        String h = hotel.reserve(name);
        String p = payment.charge(name);
        return "Booking for " + name + " -> " + String.join(" | ", f, h, p);
    }
}

