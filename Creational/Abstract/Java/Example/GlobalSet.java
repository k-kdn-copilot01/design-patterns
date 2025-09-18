public class GlobalSet extends BatchFruit {
    @Override
    Apple createApple() {
        return new AsiaApple();
    }

    Orange createOrange() {
        return new EuropeOrange();
    }
}
