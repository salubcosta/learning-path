<?php

class Car {
    private string $color;
    private int $year;

    public function __construct(string $color, int $year){
        $this->color = $color;
        $this->year = $year;
    }

    public function run(): string {
        return "The {$this->color} car is running...";
    }

    public function stop(): string {
        return "The {$this->color} car has stopped...";
    }

}

$car1 = new Car("Red", 1991);
$car2 = new Car("Yellow", 2020);

print($car1->run()  . PHP_EOL);
print($car1->stop() . PHP_EOL);

print($car2->run()  . PHP_EOL);
print($car2->stop() . PHP_EOL);

