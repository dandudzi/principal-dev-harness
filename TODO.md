# TODO

- [ ] Research and plan observability and logging support.
  - Review how coding-agent harnesses record workflow progress, step outcomes, durations, and failures. [Existing harness research](AGENT-HARNESS-RESEARCH.md)
  - Define which events to log, how to link them to a run, and how to keep credentials and raw agent conversations out of logs.
  - Recommend a logging approach and write an implementation plan.
- [ ] Research and plan workflow state management.
  - Identify the state the harness needs to track during each run.
  - Determine whether a run must resume after an interruption and which state must be saved for it to resume.
  - Recommend how to manage run state and write an implementation plan.
