<?php 

$nome = "Salumão";

echo $nome . PHP_EOL;

echo strlen($nome) . PHP_EOL;

$frutas = "pera, uva, maçã";

// strpos() - busca a posição de palavra dentro de uma string
$posicaoPalavra = strpos($frutas, "uva");
echo "A palavra uva começa na posição: {$posicaoPalavra}" . PHP_EOL;

// substr() - retorna parte da string
$parteDaString = substr($frutas, $posicaoPalavra, strlen($frutas));

echo $parteDaString . PHP_EOL;
