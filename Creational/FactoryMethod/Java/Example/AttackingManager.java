/**
 * AttackingManager - HLV ưa tấn công
 * Tạo nhiều striker để tấn công
 */
public class AttackingManager extends TeamManager {
    
    @Override
    public Player createPlayer(String playerName) {
        System.out.println("AttackingManager: Cầu thủ tấn công - " + playerName);
        return new Striker(playerName);
    }
    
    @Override
    public void executeStrategy() {
        System.out.println("AttackingManager: Thực hiện chiến thuật ép sân!");
        System.out.println("Sơ đồ: 4-2-4 (Tập trung ghi bàn)");
    }
}
