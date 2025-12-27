<?php

interface commonMethod {
    public function show();
}

class xyz implements commonMethod {
    public function show()
    {
        echo "Hi from XYZ";
    }
}

class pqr implements commonMethod {
    public function show()
    {
        echo "Hi from PQR";
    }
}

class ABC {

    private $obj = null;

    // Constructor Injection
    public function __construct(commonMethod $obj) {
        $this->obj = $obj;
    }

    public function hello()
    {
        $this->obj->show();
    }
}

// Create object using dependency injection
$obj1 = new ABC(new xyz());
$obj1->hello();   // Output: Hi from XYZ
echo "\n";

$obj2 = new ABC(new pqr());
$obj2->hello();   // Output: Hi from PQR

?>