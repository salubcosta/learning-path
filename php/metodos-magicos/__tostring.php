<?php 

class Product {

    public function __toString()
    {
        return "Você tentou printar a classe " . __CLASS__;
    }
}

$produto = new Product();

print $produto;