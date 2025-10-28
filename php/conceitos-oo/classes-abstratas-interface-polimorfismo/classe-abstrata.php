<?php

abstract class Animal {

    public function run(): string {
        return "Animal is running...";
    }

    abstract public function sound(): string;
}

class Dog extends Animal {

    public function sound(): string{
        return "Au, au...";
    }
}

$dog = new Dog();
print $dog->run();