import java.util.Scanner;

public class first {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Please enter your last name and first name separated by spaces: ");
        String name = in.nextLine();
        System.out.println("Welcome to Java Programming World, " + name);
        in.close();
    }
}
