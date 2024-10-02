import java.util.Scanner;

public class MyClass {
  public static void main(String args[]) {
      Scanner scanner = new Scanner(System.in);
      System.out.println("a: ");
      double a_ = Double.parseDouble(scanner.nextLine());
      System.out.println("b: ");
      double b_ = Double.parseDouble(scanner.nextLine());
      System.out.println("c: ");
      double c_ = Double.parseDouble(scanner.nextLine());
      scanner.close();
      double first_root = (-b_+Math.sqrt(Math.pow(b_,2)-4*a_*c_))/(2*a_);
      double second_root = (-b_-Math.sqrt(Math.pow(b_,2)-4*a_*c_))/(2*a_);
      System.out.println("Roots: "+first_root+", "+second_root);
  }
}