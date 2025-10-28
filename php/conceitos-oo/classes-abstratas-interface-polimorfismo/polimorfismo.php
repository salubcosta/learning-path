<?php

abstract class Printer {

    public function toPrint(): string {
        return "Printing data...";
    }

}

class HpPrinter extends Printer {

    public function toPrint(): string {
        return "HP Printing data...";
    }

}

class EpsonPrinter extends Printer {

    public function toPrint(): string {
        return "Epson Printing data...";
    }

}

// $printer = new Printer();
// print $printer->toPrint() . PHP_EOL;

$printer_hp = new HpPrinter();
print $printer_hp->toPrint() . PHP_EOL;

$printer_epson = new EpsonPrinter();
print $printer_epson->toPrint() . PHP_EOL;