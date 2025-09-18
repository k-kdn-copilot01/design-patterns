abstract class BatchFruit {
    Apple apple;
    Orange orange;

    void processBatch(){
        this.apple = createApple();
        this.orange = createOrange();
        apple.decorate();
        orange.decor();
    }

    abstract Apple createApple();
    abstract Orange createOrange();
}
