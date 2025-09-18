/**
 * Defender - cầu thủ hậu vệ
 */
public class Defender implements Player {
    private String name;
    
    public Defender(String name) {
        this.name = name;
    }
    
    @Override
    public void play() {
        System.out.println(name + " (Hậu vệ) đang bảo vệ khung thành và ngăn chặn các cuộc tấn công");
    }
    
    @Override
    public void specialSkill() {
        System.out.println(name + " thực hiện pha cướp bóng quan trọng và giải tòa!");
    }
    
    @Override
    public String getPosition() {
        return "Hậu vệ";
    }
    
    @Override
    public String getName() {
        return name;
    }
}
