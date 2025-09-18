/**
 * Midfielder - cầu thủ tiền vệ
 */
public class Midfielder implements Player {
    private String name;
    
    public Midfielder(String name) {
        this.name = name;
    }
    
    @Override
    public void play() {
        System.out.println(name + " (Tiền vệ) đang kiểm soát lối chơi và phân phối bóng");
    }
    
    @Override
    public void specialSkill() {
        System.out.println(name + " thực hiện đường chọc khe như sách giáo khoa cho tiền đạo!");
    }
    
    @Override
    public String getPosition() {
        return "Tiền vệ";
    }
    
    @Override
    public String getName() {
        return name;
    }
}
