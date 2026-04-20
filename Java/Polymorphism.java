import java.util.*;

class Vehicle {
    void start() {
        System.out.println("Vehicle is starting...");
    }
}

class Car extends Vehicle {
    @Override
    void start() {
        System.out.println("Car starts with a key or push button.");
    }
}

class Bike extends Vehicle {
    @Override
    void start() {
        System.out.println("Bike starts with a kick or self-start.");
    }
}

class EV extends Vehicle {
    @Override
    void start() {
        System.out.println("Electric Vehicle starts silently with a button.");
    }
}

class VehicleDemo {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Vehicle v = null;

        System.out.println("Choose Vehicle:");
        System.out.println("1. Car");
        System.out.println("2. Bike");
        System.out.println("3. Electric Vehicle");
        System.out.print("Enter choice: ");

        int choice = sc.nextInt();

        switch (choice) {
            case 1:
                v = new Car();
                break;

            case 2:
                v = new Bike();
                break;

            case 3:
                v = new EV();
                break;

            default:
                System.out.println("Invalid choice!");
                System.exit(0);
        }

        v.start();
    }
}