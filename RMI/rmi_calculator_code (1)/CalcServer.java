import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class CalcServer {
    public static void main(String[] args) {
        try {
            System.setProperty("java.rmi.server.hostname", "YOUR_EC2_PUBLIC_IP");

            Calculator calc = new CalculatorImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("CalcService", calc);

            System.out.println("RMI Calculator Server running on port 1099");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
