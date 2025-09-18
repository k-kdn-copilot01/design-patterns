/**
 * Main class để demo Factory Method pattern với ví dụ thực tế về game đá bóng
 */
public class Main {
    
    /**
     * Client code làm việc với TeamManager mà không cần biết concrete class
     */
    public static void simulateMatch(TeamManager manager, String teamName, String[] players) {
        System.out.println("=== " + teamName + " ===");
        manager.executeStrategy();
        System.out.println();
        
        manager.manageTeam(players);
        System.out.println("Hoàn thành mô phỏng trận đấu cho " + teamName + "!");
        System.out.println();
    }
    
    public static void main(String[] args) {
        System.out.println("=== Demo Ví Dụ: Game Đá Bóng Factory Method ===\n");
        
        // Danh sách cầu thủ
        String[] teamA = {"Ronaldo", "Messi", "Neymar"};
        String[] teamB = {"Ramos", "Pique", "Maldini"};
        String[] teamC = {"Modric", "Iniesta", "Pirlo"};
        
        System.out.println("🏆 MÔ PHỌNG TRẬN ĐẤU ĐÁ BÓNG 🏆\n");
        
        // Team A - Attacking strategy
        TeamManager attackingManager = new AttackingManager();
        simulateMatch(attackingManager, "Team A (Attacking)", teamA);
        
        System.out.println("─────────────────────────────────────────────────────\n");
        
        // Team B - Defensive strategy  
        TeamManager defensiveManager = new DefensiveManager();
        simulateMatch(defensiveManager, "Team B (Defensive)", teamB);
        
        System.out.println("─────────────────────────────────────────────────────\n");
        
        // Team C - Balanced strategy
        TeamManager balancedManager = new BalancedManager();
        simulateMatch(balancedManager, "Team C (Balanced)", teamC);
        
        System.out.println("─────────────────────────────────────────────────────\n");
        
        // Demonstration of polymorphism
        System.out.println("🔄 MINH HỌA TÍNH LINH HOẠT CỦA HUẤN LUYỆN VIÊN:\n");
        
        TeamManager[] managers = {
            new AttackingManager(),
            new DefensiveManager(), 
            new BalancedManager()
        };
        
        String[] singlePlayer = {"Cristiano Ronaldo"};
        
        for (int i = 0; i < managers.length; i++) {
            System.out.println("Cách tiếp cận của HLV " + (i + 1) + ":");
            managers[i].manageTeam(singlePlayer);
        }
        
        System.out.println("=== Hoàn Thành Demo Ví Dụ ===");
    }
}
