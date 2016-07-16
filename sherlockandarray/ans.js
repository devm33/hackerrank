#!/usr/bin/env node

function hasBalancePoint(A) {
    var left = 0;
    var right = A.reduce((a,b) => a+b);
    for(var i = 0; i < A.length; i++) {
        right = right - A[i];
        if(left == right) {
            return true;
        }
        left += A[i];
    }
    return false;
}

const assert = require('assert');
assert(hasBalancePoint([1,2,3,4,5,4,3,2,1]));

function processData(input) {
    input.split('\n')
    .filter((a,i) => i !== 0)
    .filter((a,i) => i % 2 !== 0)
    .map(a => a.split(' ').map(Number))
    .map(hasBalancePoint)
    .map((a => a ? 'YES' : 'NO'))
    .forEach(a => console.log(a));
} 

processData("2\n3\n1 2 3\n4\n1 2 3 3");
