<?php

class Produto {
    public $props = [];

    public function __set($name, $value){
        $this->props[$name] = $value;
    }

    public function __get($name)
    {
        return $this->props[$name];
    }
}

$produto = new Produto();

$produto->name = "Nome do produto";
$produto->price = 19.99;

echo $produto->price; # Tentando pegar um valor inexistente
// var_dump($produto->props);