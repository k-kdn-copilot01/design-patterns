/**
 * DefensiveManager - HLV ưa phòng thủ
 * Tạo nhiều defender để bảo vệ khung thành
 */
public class DefensiveManager extends TeamManager {
    
    @Override
    public Player createPlayer(String playerName) {
        System.out.println("DefensiveManager: Cầu thủ phòng thủ - " + playerName);
        return new Defender(playerName);
    }
    
    @Override
    public void executeStrategy() {
        System.out.println("DefensiveManager: Thực hiện chiến thuật phòng thủ đổ bê tông!");
        System.out.println("Sơ đồ: 5-4-1 (Tập trung ngăn chặn bàn thắng)");
    }
}
