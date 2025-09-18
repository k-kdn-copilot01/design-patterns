//public class Main {
//    public static void main(String[] args) {
//        System.out.println("=== Structure Demo: Singleton Implementations ===\n");
//
//        // Lazy Singleton
//        System.out.println("1. Lazy Singleton:");
//        LazySingleton lazy1 = LazySingleton.getInstance();
//        LazySingleton lazy2 = LazySingleton.getInstance();
//        System.out.println("lazy1 == lazy2: " + (lazy1 == lazy2));
//        lazy1.doSomething();
//        System.out.println();
//
//        // Eager Singleton
//        System.out.println("2. Eager Singleton:");
//        EagerSingleton eager1 = EagerSingleton.getInstance();
//        EagerSingleton eager2 = EagerSingleton.getInstance();
//        System.out.println("eager1 == eager2: " + (eager1 == eager2));
//        eager1.doSomething();
//
//        System.out.println("\n=== Structure Demo Complete ===");
//    }
//}