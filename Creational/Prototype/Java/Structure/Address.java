public class Address implements Prototype {
	private String street;
	private String district;
	private String province;

	public Address(String street, String district, String province) {
		this.street = street;
		this.district = district;
		this.province = province;
	}

	public void setProvince(String province) {
		this.province = province;
	}

	@Override
	public String toString() {
		return "Address [street=" + street + ", district=" + district + ", province=" + province + "]";
	}

	@Override
	public Prototype clone() {
		return new Address(this.street, this.district, this.province);
	}
}