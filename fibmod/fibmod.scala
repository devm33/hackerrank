#!/bin/sh
exec scala "$0" "$@"
!#

object Solution {

    def fibMod(a: BigInt, b: BigInt, n: Int): BigInt = n match {
        case 2 => b
        case _ => fibMod(b, b * b + a, n - 1)
    }

    def main(args: Array[String]) {
        val Array(a, b, n) = scala.io.StdIn.readLine.split(" ").map(_.toInt)
        println(fibMod(a, b, n))
    }
}
