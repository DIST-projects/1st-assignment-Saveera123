import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class CalcClient {
    public static void main(String[] args) {
        try {
            String serverIP = "YOUR_EC2_PUBLIC_IP";

            Registry registry = LocateRegistry.getRegistry(serverIP, 1099);
            Calculator calc = (Calculator) registry.lookup("CalcService");

            System.out.println("Add: " + calc.add(10, 5));
            System.out.println("Sub: " + calc.sub(10, 5));
            System.out.println("Mul: " + calc.mul(10, 5));
            System.out.println("Div: " + calc.div(10, 5));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
