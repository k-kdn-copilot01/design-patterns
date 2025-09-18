public class AfricaSet extends BatchFruit{
    @Override
    Apple createApple() {
        return new AfricaApple();
    }

    @Override
    Orange createOrange() {
        return new CanadaOrange();
    }

}
