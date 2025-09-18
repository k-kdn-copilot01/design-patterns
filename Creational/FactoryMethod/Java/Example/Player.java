/**
 * Player interface - đại diện cho cầu thủ trong game đá bóng
 */
public interface Player {
    /**
     * Hành động chính của cầu thủ
     */
    void play();
    
    /**
     * Kỹ năng đặc biệt của cầu thủ
     */
    void specialSkill();
    
    /**
     * Lấy vị trí của cầu thủ
     */
    String getPosition();
    
    /**
     * Lấy tên của cầu thủ
     */
    String getName();
}
