# Principal Dev Harness

Principal Dev Harness coordinates coding workflows that help teams produce high-quality code. A workflow file defines how to combine small scripts and configure each step. Each script can run on its own.

The coordinator delegates coding tasks to existing agent harnesses such as Codex and OpenCode. Those harnesses manage their own model calls and tools.

## Run tests

From the repository root, use [mise](https://mise.jdx.dev/) to install Python and run the tests.

```sh
mise install --locked
mise exec -- python -m unittest discover -s tests -v
```

Put Python scripts in `scripts/` and add test modules named `test_*.py` in `tests/`. The starter test checks that the scripts directory exists and that its Python files compile.

GitHub Actions runs the same test command on pull requests and pushes to `master`.
