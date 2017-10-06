package main

import "golang.org/x/tour/reader"

type MyReader struct{}

func (mr MyReader) Read(b []byte) (int, error) {
	return len(b)
}

func main() {
	reader.Validate(MyReader{})
}
