# Conventional Commits Patterns 📊
See full description at [Conventional Commits Pattern](https://github.com/BrunoTanabe/conventional-commits-pattern/).

## 1. Introduction
Conventional Commits is a specification for writing consistent commit messages. It defines a set of rules for creating an explicit commit history, which makes it easier to write automated tools on top of. These patterns are meant to improve the readability and structure of commit messages, thereby facilitating better collaboration and project management.

## 2. Commit Types
Conventional Commits Patterns include several types, each serving a specific purpose:

- **fix**: Patches a bug in your codebase.
- **feat**: Introduces a new feature to the codebase.
- **docs**: Documentation only changes.
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc).
- **refactor**: A code change that neither fixes a bug nor adds a feature.
- **perf**: Improves performance.
- **test**: Adds missing tests or corrects existing tests.
- **build**: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm).
- **ci**: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs).
- **chore**: Other changes that don't modify src or test files.
- **wip**: Work in progress; not yet ready for production.

## 3. Examples
Each commit message example includes a Bash command to demonstrate how to create the commit using Git.

### fix
```bash
git commit -m "fix(order): correct minor typos in code

see the issue for details on the typos fixed"
```
### feat
```bash
git commit -m "feat(blog): add comment section

Users can now leave comments on articles. This was a highly requested feature from our user feedback."
```
### docs
```bash
git commit -m "docs(changelog): update changelog to 0.3.0"
```
### style
```bash
git commit -m "style(navbar): correct indentation"
```
### refactor
```bash
git commit -m "refactor(auth): simplify validation logic"
```
### perf
```bash
git commit -m "perf(rendering): cache SVG assets"
```
### test
```bash
git commit -m "test(login): add unit tests for password reset"
```
### build
```bash
git commit -m "build(packer): update dependencies"
```
### ci
```bash
git commit -m "ci(travis): force install dependencies"
```
### chore
```bash
git commit -m "chore(release): bump version to 1.0.3"
```
### wip
```bash
git commit -m "wip(feature-x): temporary commit - to be squashed"
```