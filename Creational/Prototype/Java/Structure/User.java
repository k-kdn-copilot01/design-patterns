public class User implements Prototype {
	private String firstName;
	private String lastName;
	private Address address;

	public User(String firstName, String lastName, Address address) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.address = address;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public void setAddress(Address address) {
		this.address = address;
	}

	@Override
	public String toString() {
		return "User[" + this.firstName + ", " + this.lastName + ", " + this.address.toString() + "]";
	}

	@Override
	public Prototype clone() {
		return new User(this.firstName, this.lastName, this.address.clone());
	}
}