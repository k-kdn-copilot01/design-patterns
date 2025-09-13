public class Main {
    public static void main(String[] args) {
			Address address = new Address("street", "district", "HN");
			User user = new User("First", "Last", address);

			Address address2 = address.clone();
			address2.setProvince("DN");

	    User user2 = user.clone();
			user2.setFirstName("First2");
	    user2.setAddress(address2);

	    System.out.println(user.toString());
	    System.out.println(user2.toString());
    }
}