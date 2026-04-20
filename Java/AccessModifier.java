class BankAccount {

    private String name;
    private double balance;

    public BankAccount(String name, double balance) {
        this.name = name;
        this.balance = balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println(amount + " deposited successfully.");
        } else {
            System.out.println("Invalid deposit amount!");
        }
    }

    public double getBalance() {
        return balance;
    }

    public void display() {
        System.out.println("Account Holder: " + name);
        System.out.println("Balance: " + balance);
    }
}

class BankDemo {
    public static void main(String[] args) {

        BankAccount acc = new BankAccount("John", 10000);
        acc.display();
        acc.deposit(5000);
        System.out.println("Final Balance: " + acc.getBalance());
    }
}