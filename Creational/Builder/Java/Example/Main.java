public class Main {
    public static void main(String[] args) {
        ComputerDirector director = new ComputerDirector();

        ComputerBuilder officeBuilder = new OfficeComputerBuilder();
        director.buildBasicPC(officeBuilder, "Intel Core i5", 16, 512, true, "Windows 11 Pro");
        Computer officePC = officeBuilder.getResult();

        ComputerBuilder gamingBuilder = new GamingComputerBuilder();
        director.buildBasicPC(gamingBuilder, "AMD Ryzen 7", 32, 2000, true, "Windows 11 Home");
        Computer gamingPC = gamingBuilder.getResult();

        System.out.println("Office PC: " + officePC);
        System.out.println("Gaming PC: " + gamingPC);
    }
}