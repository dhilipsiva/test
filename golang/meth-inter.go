package main

import (
	"fmt"
	"math"
)

type Foo struct {
	bar float64
	baz float64
}

type Vertex struct {
	X   float64
	Y   float64
	foo Foo
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func (v *Vertex) Scale(i int) {
	v.X = v.X * float64(i)
	v.Y = v.Y * float64(i)
	v.foo.bar = v.foo.bar * float64(i)
	v.foo.baz = v.foo.baz * float64(i)
}

func main() {
	foo := Foo{3, 4}
	v := Vertex{X: 3, Y: 5, foo: foo}
	fmt.Println(v.Abs())
	fmt.Println(v.foo)
	v.Scale(10)
	fmt.Println(v.Abs())
	fmt.Println(v.foo)
}
