# Principal Dev Harness context

Use these terms in code and project documentation.

Principal Dev Harness runs coding workflows. A workflow file defines the steps and how to configure them. A coding task delegates coding work to an agent harness such as Codex or OpenCode. The agent harness manages its model calls and tool use.

## Workflow terms

| Term | Meaning |
| --- | --- |
| Workflow | A definition of the steps that make up a coding process. |
| Workflow file | A file that defines a workflow and its step configuration. |
| Workflow step | A configured unit of work in a workflow. A step can run a script. |
| Coding task | A specialized workflow step that delegates coding work to an agent harness. |
| Script | A Python program that does a specific job. It can run on its own or as part of a workflow. |
| Workflow run | One execution of a workflow. The same workflow can have many runs. |
| Agent harness | An existing system, such as Codex or OpenCode, that does coding work and manages its model calls and tool use. |

## Run terms

| Term | Meaning |
| --- | --- |
| Run state | The information that describes a workflow run at a given time, including its progress and known step outcomes. |
| Step outcome | The result of a workflow step in a specific run, such as success or failure. |
| Run event | A record of something that occurs during a workflow run, such as a step starting or failing. |
