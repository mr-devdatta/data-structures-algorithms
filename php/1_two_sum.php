<?php
include_once __DIR__ . '../helper.php';

/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

*/


/**
 * Brute-force two-sum solution using nested loops.
 * Time complexity: O(n^2), Space complexity: O(1)
 * Returns an array with two indices whose values add up to $target.
 */
function twoSum($nums, $target)
{
    $finalArr = [];
    $count = count($nums);
    for ($i = 0; $i < $count; $i++) {
        for ($j = $i + 1; $j < $count; $j++) {
            if ($target == (int) $nums[$i] + $nums[$j]) {
                $finalArr = [$i, $j];
                break;
            }
        }
    }

    return $finalArr;
}

/**
 * Optimized two-sum using a single-pass hash map (associative array).
 * Time complexity: O(n), Space complexity: O(n)
 * Returns an array with two indices whose values add up to $target.
 */
function twoSumOptimized($nums, $target)
{
    $map = []; // value => index
    foreach ($nums as $i => $num) {         
        $complement = $target - $num;
        //echo "i = $i, target = $target,  num = $num, complement = $complement\n";
        echo "( ". $target . " - " . $num . " ) = " . $complement . "\n";

        if (isset($map[$complement])) {
            return [$map[$complement], $i];
        }
        // store the index of the current number
        $map[$num] = $i;
        pre($map);
    }

    // If no solution found (per problem constraints this shouldn't happen), return empty array
    return [];
}


$nums = [1, 2, 3, 5, 7, 11, 15, 17, 21, 34, 35, 56, 78, 99, 100, 150, 200];
$target = 177;
print_r(twoSumOptimized($nums, $target));
