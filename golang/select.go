package main

import (
	"fmt"
)

func fibonacci(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case <-quit:
			fmt.Println("cq")
			return
		case c <- x:
			fmt.Println("cc")
			x, y = y, x+y

		}
	}
}

func main() {
	c := make(chan int)
	quit := make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println("FOR")
			fmt.Println(<-c)
			if i == 5 {
				quit <- 0
				fmt.Println("===")
			}
		}
		fmt.Println("quit")
	}()
	fibonacci(c, quit)
}
