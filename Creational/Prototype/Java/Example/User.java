public class User implements Prototype {
    private String name;
    private Integer age;

    public User(String name, Integer age) {
        this.name = name;
        this.age = age;
    }

    public User clone(){
        return new User(this.name, this.age);
    }
}
