package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println("call SolveNQueens")
}

func PrintQueens(q []string) {
	fmt.Println()
	for i, v := range q {
		fmt.Println(i, v)
	}
	fmt.Println()
}

func stringQueen(q []int) []string {
	r := make([]string, len(q))
	b := strings.Repeat(".", len(q))
	for i, v := range q {
		r[i] = b[:v] + "Q" + b[v+1:]
	}
	return r
}

func stringQueens(q [][]int) [][]string {
	r := make([][]string, len(q))
	for i, v := range q {
		r[i] = stringQueen(v)
	}
	return r
}

func abs(i int) int {
	if i < 0 {
		return -i
	}
	return i
}

func safeToAdd(a int, q []int) bool {
	n := len(q)
	for i, v := range q {
		if v == a || abs(i-n) == abs(v-a) {
			return false
		}
	}
	return true
}

func SolveNQueens(n int) [][]string {
	q := make([][]int, n)
	for i := 0; i < n; i++ {
		q[i] = []int{i}
	}

	o := make([][]int, 0)
	var c []int
	for len(q) > 0 {
		c = q[0]
		q = q[1:]
		if len(c) == n {
			o = append(o, c)
			continue
		}
		for i := 0; i < n; i++ {
			if safeToAdd(i, c) {
				q = append(q, append(c, i))
			}
		}
	}
	return stringQueens(o)
}
