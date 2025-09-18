public interface MarketBuiler {
    MarketBuiler buildFishStall(Integer size);
    MarketBuiler buildCookieStall(Integer size);
    MarketBuiler buildChickenStall(Integer size);
    Market getResult();
}
