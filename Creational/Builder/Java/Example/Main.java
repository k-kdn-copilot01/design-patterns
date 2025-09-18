/*
Our problem

Build the market
The market can sell many types of things, like fish, chicken, pork, ...
Because of this variety, it's better to build the market part by part, from stall to stall
 */


public class Main {
    public static void main(String[] args) {
        MarketBuiler builder = new MarketContractor1();
        builder
                .buildFishStall(2)
                .buildChickenStall(3);

        System.out.println(builder.getResult().getChickenStall());

        // In the future, if this creation logic get over and over again, we need to wrap this logic for that
        MarketBuiler builder1 = new MarketContractor1();
        MarketDirector director = new MarketDirector();
        director.buildNormalMarket(builder1);
        System.out.println(builder1.getResult().getChickenStall());
    }
}