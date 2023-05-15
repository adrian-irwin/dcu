public class BankAccount {
    double balance;

    public BankAccount(){
        balance = 100.0;
    }

    public BankAccount(double bal){
        balance = bal;
    }

    public void withdraw(double amount) {
        balance -= amount;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public String toString() {
        return "The balance is " + balance;
    }
}
