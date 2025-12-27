<?php


function pre($arr, $flg = 0)
{
    echo "<pre>";
    print_r($arr);
    echo "</pre>";
    echo "------------------------------------\n";

    if ($flg == 1) {
        die();
    }
}

function text(...$args)
{
    $str = "";
    if (!empty($args)) {
        foreach ($args as $arg) {
            if (is_array($arg)) {
                $arg = " >>> ". json_encode($arg). " <<< ";
            }
            $str .=  $arg . ",   ";
        }
        echo rtrim($str, ", ") . '\n';
    } else {
        echo "------------------------------------\n";
    }
}
