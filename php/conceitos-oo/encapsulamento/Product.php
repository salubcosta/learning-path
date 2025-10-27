<?php

class Product {
    private string $name;
    private string $description;
    private string $category;
    private float $price;

    public function setName(string $name) {
        $this->name = $name;
    }

    public function setDescription(string $description) {
        $this->description = $description;
    }

    public function setCategory(string $category) {
        $this->category = $category;
    }

    public function setPrice(float $price) {
        $this->price = $price;
    }

    public function getName(): string {
        return $this->name;
    }

    public function getDescription(): string {
        return $this->description;
    }

    public function getCategory(): string {
        return $this->category;
    }

    public function getPrice(): float {
        return $this->price;
    }
}