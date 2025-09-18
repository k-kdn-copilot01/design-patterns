/*
This exercise is about store problem
Currently, the shop only sell watermelon
Now, we still want the app for shop that sell coconut (or the previous shop decide to sell coconut).
What should we code so that we don't have to change so much code?

Because the procedure of selling each fruit is the same
   Prepare food

   Transfer food

   Get money

But the detail maybe different
    The watermelon's prepare food is different from coconut
    ...

=> we may think about Factory pattern
 */

public class Main {
    public static void main(String[] args) {
        Shop shop;
        String system_fruit = "coconut";
        if(system_fruit == "coconut"){
            shop = new CoconutShop();
        } else {
            shop = new WatermelonShop();
        }

        shop.sell();
    }
}