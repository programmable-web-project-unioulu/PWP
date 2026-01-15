import java.util.

public class first {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Please enter your last name and first name: ");
        String name = in.nextLine();
        System.out.println("Welcome to Java Programming World, " + name);
        System.out.println("Good Luck," + name);
        in.close();
    }
}
