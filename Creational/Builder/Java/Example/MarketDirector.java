public class MarketDirector {
    public void buildNormalMarket(MarketBuiler builder) {
        builder
                .buildFishStall(1)
                .buildChickenStall(1);
    }

    public void buildBigMarket(MarketBuiler builder) {
        builder
                .buildFishStall(2)
                .buildChickenStall(2)
                .buildCookieStall(2);
    }
}
