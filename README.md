## Branch prefix pre-commit hook

This hook adds a prefix to a branch name when it does not have one.

### Install
In your `.pre-commit-config` add the following lines:

```yaml
- repo: https://github.com/JadHADDAD92/branch-prefix
  rev: "0.1.0"
  hooks:
    - id: branch-prefix
    - default_stages: [push]
```
This will trigger the hook when pushing your commits.

If `pre-push` hook is not installed, install using: `pre-commit install --hook-type pre-push`

### Configuration

At the root of your project, add `branch-prefix.yaml`. For example:
```yaml
prefix: jad
separator: /
ignore-branches: [main, master]
ignore-branches-starting-with: [v., "2022"]
```

* **prefix**: prefix to prepend a branch name with
* **separator**: separator between prefix and branch name
* **ignore-branches**: list of branches to ignore and leave as they are
* **ignore-branches-starting-with**: list of patterns at the beginning of a branch name to ignore (these are case **insensitive**)

In the previous example:
* if branch name is `feature`, it will be renamed to `jad/feature`.
* if branch name is `main`, it will be remain the same.
* if branch name is `2022.11.24`, it will be remain the same since the beginning matches with `2022`.
* if branch name is `V5.2`, it will be remain the same since the beginning matches with `v.` (case insensitive).
