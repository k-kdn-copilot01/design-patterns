public class Main {
   public static void main(String[] args) {
       Builder man1 = new ConcreteBuilder1();

       man1
               .buildPart1("Bacony")
               .buildPart2("Root")
               .buildPart3("Bedroom");

       System.out.println(man1.getResult().getPart3());

   }
}