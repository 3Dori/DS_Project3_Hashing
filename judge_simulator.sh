#!/bin/bash
testname='./test'
input='_input.txt'
expected_result='_expected_result.txt'
actual_result='_actual_result.txt'
program='./gen_hash.py'

for i in {1..4}
do
    cat $testname$i$input | $program > $testname$i$actual_result
    diff -u $testname$i$expected_result $testname$i$actual_result
done
