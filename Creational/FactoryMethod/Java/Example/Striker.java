/**
 * Striker - cầu thủ tấn công
 */
public class Striker implements Player {
    private String name;
    
    public Striker(String name) {
        this.name = name;
    }
    
    @Override
    public void play() {
        System.out.println(name + " (Tiền đạo) đang tấn công và tìm kiếm cơ hội ghi bàn");
    }
    
    @Override
    public void specialSkill() {
        System.out.println(name + " thực hiện sút mạnh vào khung thành!");
    }
    
    @Override
    public String getPosition() {
        return "Tiền đạo";
    }
    
    @Override
    public String getName() {
        return name;
    }
}
