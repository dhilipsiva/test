package main

import "fmt"

type Float float64

type Abser interface {
	Abs() int
}

func (f Float) Abs() int {
	return int(f)
}

func main() {
	var a Abser
	a = Float(2.4)
	fmt.Println(a.Abs())
}
