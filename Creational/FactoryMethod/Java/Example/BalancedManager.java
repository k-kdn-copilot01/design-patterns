/**
 * BalancedManager - HLV cân bằng
 * Tạo midfielder để kiểm soát trận đấu
 */
public class BalancedManager extends TeamManager {
    
    @Override
    public Player createPlayer(String playerName) {
        System.out.println("BalancedManager: Cầu thủ tiền vệ - " + playerName);
        return new Midfielder(playerName);
    }
    
    @Override
    public void executeStrategy() {
        System.out.println("BalancedManager: Thực hiện chiến thuật phòng ngự phản công!");
        System.out.println("Sơ đồ: 4-4-2 (Vừa tấn công và phòng thủ)");
    }
}
