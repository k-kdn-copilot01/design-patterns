/*
Define the problem that want to solve

The fruit shop want to sell fruit by set - A set contain only apple, orange but the type of fruit can range from different countries like Aisa and Europe.
In the future, the set can be extended to more fruit - for example: Coconut from Africa

More knowledge: the fixed here is the kind of fruit. the contries can not be the same!
Problem: Can we handle both set with 3 fruits and set with 2 fruits

 */
public class Main {
    public static void main(String[] args) {
        BatchFruit africaSet = new AfricaSet();
        africaSet.processBatch();

        BatchFruit globalSet = new GlobalSet();
        globalSet.processBatch();
    }
}