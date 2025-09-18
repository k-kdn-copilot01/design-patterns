package Creational.Builder.Java.Structure;

public class Main {
    public static void main(String[] args) {
        SampleObject obj = new SampleObject.Builder()
                .setField1("value1")
                .setField2("value2")
                .build();

        System.out.println(obj.getField1() + " " + obj.getField2() + " " + obj.getField3());
    }
}
