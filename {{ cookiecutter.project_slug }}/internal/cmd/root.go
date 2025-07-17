package cmd

import (
	"os"
	"fmt"
	"errors"

	"github.com/spf13/cobra"
)

type ExitCodeError struct {
	ExitCode int
}

func (e ExitCodeError) Error() string {
	return fmt.Sprintf("exit code %d", e.ExitCode)
}

func Execute() int {
	if err := execute(); err != nil {
		var exitCodeErr ExitCodeError
		if errors.As(err, &exitCodeErr) {
			return exitCodeErr.ExitCode
		}

		fmt.Fprintf(os.Stderr, "error: %v\n", err)
		return 1
	}
	return 0
}

func execute() error {
	root := &cobra.Command{
		Use:   "{{ cookiecutter.project_slug }}",
		SilenceUsage: true,
		SilenceErrors: true,
		RunE: func(cmd *cobra.Command, args []string) error {
			fmt.Println("Hello, World!")
			return nil
		},
	}

	return root.Execute()
}
