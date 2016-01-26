//
// test.go
// Copyright (C) 2016 dhilipsiva <dhilipsiva@gmail.com>
//
// Distributed under terms of the MIT license.
//

package foo

import "fmt"

func foo() {
	fmt.Println("Foo!")
}

func poo() {
	fmt.Println("Wow!")
	foo()
}
