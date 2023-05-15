public class TestBankAccount {
    public static void main(String [] args) {
        BankAccount account = new BankAccount(); // This uses the default constructor.

      System.out.println(account);
      account.withdraw(25);

      System.out.println(account);

    }
}
