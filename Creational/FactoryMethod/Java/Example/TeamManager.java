/**
 * TeamManager abstract class - quản lý đội bóng
 * Định nghĩa factory method để tạo cầu thủ
 */
public abstract class TeamManager {
    
    /**
     * Factory Method - tạo cầu thủ theo chiến thuật của từng HLV
     */
    public abstract Player createPlayer(String playerName);
    
    /**
     * Business logic - quản lý đội bóng
     */
    public void manageTeam(String[] playerNames) {
        System.out.println("Manager: Đang thiết lập đội hình...");
        
        for (String playerName : playerNames) {
            Player player = createPlayer(playerName);
            System.out.println("Manager: " + player.getName() + " được phân công vào vị trí " + player.getPosition());
            
            // Cầu thủ thực hiện hành động
            player.play();
            player.specialSkill();
            System.out.println();
        }
        
        System.out.println("Manager: Hoàn thành thiết lập đội hình!");
    }
    
    /**
     * Chiến thuật chung của đội
     */
    public void executeStrategy() {
        System.out.println("Manager: Thực hiện chiến thuật đội...");
    }
}
