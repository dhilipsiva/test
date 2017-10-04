package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X float64
	Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func (v *Vertex) Scale(i int) {
	v.X = v.X * float64(i)
	v.Y = v.Y * float64(i)
}

func main() {
	v := Vertex{X: 3, Y: 5}
	fmt.Println(v.Abs())
	v.Scale(10)
	fmt.Println(v.Abs())
}
