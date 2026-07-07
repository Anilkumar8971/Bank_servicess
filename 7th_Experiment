package com.bnmit;

class BankAccount {
    private double balance;

    public BankAccount(double initialBalance) {
        if (initialBalance < 0) {
            throw new IllegalArgumentException("Initial balance cannot be negative");
        }
        this.balance = initialBalance;
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit must be positive");
        }
        balance += amount;
    }

    public void withdraw(double amount) {
        if (amount <= 0 || amount > balance) {
            throw new IllegalArgumentException("Invalid withdrawal");
        }
        balance -= amount;
    }

    public double getBalance() {
        return balance;
    }
}

public class BankService {

    public static void main(String[] args) {

        BankAccount acc = new BankAccount(1000);

        System.out.println("Initial Balance : " + acc.getBalance());

        acc.deposit(500);
        System.out.println("Balance after Deposit : " + acc.getBalance());

        acc.withdraw(300);
        System.out.println("Balance after Withdrawal : " + acc.getBalance());

        System.out.println("Final Balance : " + acc.getBalance());
    }
}
