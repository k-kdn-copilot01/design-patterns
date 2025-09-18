public class Main {
   public static void main(String[] args) {
       String system_value = null; // To define which set will be used

       Factory setProduct = new FactorySetA1B2();
       setProduct.handleBatchProduct();
   }
}