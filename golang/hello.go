package main

import "fmt"

func add(num1 int, num2 int) int {
	return num1 + num2
}

type Point struct {
	x int
	y int
}

func main() {
	/*
		fmt.Println("Hello World", add(12, 13))
		for i := 0; i < 10; i++ {
			fmt.Println(i)
		}

		var x int = 5
		fmt.Println(x)
		p := &x
		fmt.Println(*p)
		*p = 9
		fmt.Println(x, *p)
		p * Point = Point{5, 4}
		p := Point{y: 5, x: 4}
		fmt.Println(p.x)

		var a [2]int
		a[0] = 1
		a[1] = 2
		b := []int{1, 2, 3, 4, 5, 6}
		c := b[3:4]
		fmt.Println(a)
		fmt.Println(b)
		fmt.Println(c, len(c), cap(c))

		var d = make([]int, 3)
		d = append(d, 5, 6, 7, 'a')
		for i, v := range d {
			fmt.Println(i, v)
		}

		var f = make([][]int, 3, 4)
		fmt.Println(f)
	*/
	m := make(map[string]int)
	m["FOO"] = 1
	m["BAR"] = 2
	val, exists := m["BAR"]
	if exists {
		fmt.Println("Exists", val)
	} else {
		fmt.Println("Nope")
	}
	delete(m, "BAR")
	val, exists = m["BAR"]
	if exists {
		fmt.Println("Exists", val)
	} else {
		fmt.Println("Nope")
	}
	// p * Point = Point{5, 4}
	p := Point{y: 5, x: 4}
	v := &p
	v.x = 100
	fmt.Println(p)
	fmt.Println(v)
}
