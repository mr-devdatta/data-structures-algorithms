<?php 
class Singleton {
    private static $instance = null;
    public static $cnt = 0;

    private function __construct()
    {
        // private function
    }

    public static function getInstance()
    {
        if(self::$instance == null) {
            //self::$instance = new self();
            self::$instance = new Singleton();
        }

        self::$cnt += 1;
        return self::$instance;

    }

}

$obj1 = Singleton::getInstance();
echo Singleton::$cnt;
$obj2 = Singleton::getInstance();
$obj3 = Singleton::getInstance();
$obj4 = Singleton::getInstance();

echo Singleton::$cnt;

?>