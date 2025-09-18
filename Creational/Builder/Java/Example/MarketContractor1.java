public class MarketContractor1 implements MarketBuiler{
    private Market market = new Market();

    @Override
    public MarketBuiler buildFishStall(Integer size) {
        this.market.setFishStall(size);
        return this;
    }

    @Override
    public MarketBuiler buildCookieStall(Integer size) {
        this.market.setCookieStall(size);
        return this;
    }

    @Override
    public MarketBuiler buildChickenStall(Integer size) {
        this.market.setChickenStall(size);
        return this;
    }

    @Override
    public Market getResult() {
        return market;
    }
}
