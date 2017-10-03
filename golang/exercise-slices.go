package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
	a := make([][]uint8, dx)
	for x := 0; x < dx; x++ {
		d := make([]uint8, dy)
		for y := 0; y < dy; y++ {
			d[y] = uint8((x + y) / 2)
		}
		a[x] = d
	}
	return a
}

func main() {
	pic.Show(Pic)
}
