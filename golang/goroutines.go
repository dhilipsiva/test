package main

import (
	"fmt"
	// "time"
)

func say(s string, repeat int, timeout int, res chan int) {
	for i := 0; i < repeat; i++ {
		// time.Sleep(time.Duration(timeout) * time.Millisecond)
		fmt.Println(s)
	}
	res <- repeat
}

func main() {
	res := make(chan int)
	fmt.Println("BEFORE GO")
	go say("first", 20, 200, res)
	fmt.Println("BETWEEN GO")
	go say("second", 20, 250, res)
	fmt.Println("AFTER GO")
	fmt.Println("AFTER GO RES")
	// r1, r2 := <-res, <-res
	r1 := <-res
	fmt.Println("BETWEEN GO RES")
	r2 := <-res
	fmt.Println("AFTER GO RES")
	fmt.Println(r1, r2)
}
