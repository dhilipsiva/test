//
// test.go
// Copyright (C) 2016 dhilipsiva <dhilipsiva@gmail.com>
//
// Distributed under terms of the MIT license.
// A program to see func declaration withing func works or not
//

package main

import "fmt"

func main() {

	func foo() {  // Apparently this is not allowed! :P
		fmt.Println("Foo!")
	}

	fmt.Println("Wow!")
	foo()
}
