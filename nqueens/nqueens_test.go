package main

import (
	"testing"
)

func Test4Queens(t *testing.T) {
	soln := SolveNQueens(4)
	if len(soln) != 2 {
		t.Error("Expected two solutions to 4Queens")
	}
	soln1 := []string{
		".Q..",
		"...Q",
		"Q...",
		"..Q.",
	}
	soln2 := []string{
		"..Q.",
		"Q...",
		"...Q",
		".Q..",
	}
	expected := [][]string{soln1, soln2}

	has := hasSolns(soln, expected)
	if !has {
		t.Error("missing solution(s)")
		for _, v := range soln {
			PrintQueens(v)
		}
	}
}

func Test6Queens(t *testing.T) {
	soln := SolveNQueens(6)
	if len(soln) != 4 {
		t.Error("Expected 4 solutions to 6Queens")
	}
	expected := [][]string{
		[]string{".Q....", "...Q..", ".....Q", "Q.....", "..Q...", "....Q."},
		[]string{"..Q...", ".....Q", ".Q....", "....Q.", "Q.....", "...Q.."},
		[]string{"...Q..", "Q.....", "....Q.", ".Q....", ".....Q", "..Q..."},
		[]string{"....Q.", "..Q...", "Q.....", ".....Q", "...Q..", ".Q...."},
	}
	has := hasSolns(soln, expected)
	if !has {
		t.Error("missing solution(s)")
		for _, v := range soln {
			PrintQueens(v)
		}
	}
}

func hasSolns(s [][]string, e [][]string) bool {
	var has bool
	for _, a := range e {
		has = false
		for _, b := range s {
			if equals(a, b) {
				has = true
				break
			}
		}
		if !has {
			return false
		}
	}
	return true
}

func equals(a []string, b []string) bool {
	for i, v := range a {
		if v != b[i] {
			return false
		}
	}
	return true
}
