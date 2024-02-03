package main

import "fmt"

func main() {
	var x, y int

	fmt.Scanf("%d %d", &x, &y)
	if x > y {
		fmt.Println(">")
	} else if x < y {
		fmt.Println("<")
	} else {
		fmt.Println("==")
	}
}
