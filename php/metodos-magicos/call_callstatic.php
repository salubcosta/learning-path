<?php

class Product
{
    /**
     * @name - nome do método chamado
     * @arguments - array com os argumentos
     */
    public function __call($name, $arguments)
    {
        print_r([$name,$arguments]);
    }

    public static function __callStatic($name, $params)
    {
        print_r([$name,$params]);
    }
}


$product = new Product();

$product->metodoInvalido("Valor 1", 19.99);

/**
 * Apenas com o __call, eu consigo tratar chamadas de métodos inexistentes.
 * Quando for utilizar métodos estáticos, vou precisar utilizar o callstatic
 */

Product::getConnection();