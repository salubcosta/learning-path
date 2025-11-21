<?php 

/**
 * 1. Crie um array chamado cidades contendo o nome de 5 cidades. Imprima o nome da terceira cidade.
 */
$cidade = ["Palmas","Taguatinga","Araguaína","Brasília","Aragominas"];
print $cidade[2] . PHP_EOL;

/**
 * 2. Crie um array associativo cuja chaves são nome de três alunos e os valores são as idades deles. Imprima a idade do segundo aluno
 */
$alunos = [
    "Mariana" => 6,
    "Beatriz" => 6,
    "Maria" => 5
];
print $alunos["Beatriz"] . PHP_EOL;

/**
 * 3. Crie um array de cores contendo 3 cores, adicione uma cor no final e remova a primeira cor. Imprima o array
 */

$cores = ["Vermelho", "Laranja", "Verde"];

array_push($cores, "Preto");

array_shift($cores);

print_r($cores);