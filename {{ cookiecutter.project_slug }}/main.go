package main

import (
	"os"

	"{{ cookiecutter.go_module }}/internal/cmd"
)

func main() {
	os.Exit(cmd.Execute())
}
