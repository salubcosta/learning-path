<?php

class Animal {
    private string $name;

    public function sleep() {
        return $this->name . " are sleeping...";
    }

    public function setName(string $name){
        $this->name = $name;
    }
}

class Dog extends Animal {

    public function sleep(){
        print parent::sleep();
        return "It's a dog...";
    }
}

$dog = new Dog();
$dog->setName("Ted");

print $dog->sleep();