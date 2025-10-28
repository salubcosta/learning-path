<?php
namespace xpto;

interface Animal {
    public function run(): string;
    public function sound(): string;
}

class Dog implements \xpto\Animal {

    public function run(): string { return "Dog is running"; }
    public function sound(): string { return "Au, au..."; }

}

$dog = new Dog();
print $dog->run() . PHP_EOL;
print $dog->sound();