<?php

class BankAccount {
    private float $balance = 0; 

    public function deposit(float $money) {
        $this->balance += $money;
    }

    public function withDraw(float $money) {
        if($money > $this->balance) {
            throw new Exception("Saque não permitido!",1);
        }

        $this->balance -= $money;
    }

    public function getBalance(): float {
        return $this->balance;
    }
}

$bankAccount = new BankAccount();
$bankAccount->deposit(10);
print("Saldo: " . $bankAccount->getBalance()) . PHP_EOL;
$bankAccount->withDraw(10);
print("Saldo: " . $bankAccount->getBalance()) . PHP_EOL;
