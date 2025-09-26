package Creational.Facade.Java.Example;

public class Client {
    public String run() {
        // Direct interaction
        String direct = String.join(" + ",
                new FlightBooking().book("Alice"),
                new HotelBooking().reserve("Alice"),
                new PaymentGateway().charge("Alice"));
        direct = "Direct: " + direct;

        // Via facade
        TravelFacade facade = new TravelFacade();
        String viaFacade = "Facade: " + facade.bookTrip("Alice");

        return String.join(System.lineSeparator(), direct, viaFacade);
    }
}

