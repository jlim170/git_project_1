# Learnings
## Checkpoint 1
### Commands
```
pytest tests/
git status
git add tests/test_calculator.py
git commit -m "fix"
git add .gitignore
git commit -m "update"
git push -u origin feature/mnguye31
```
### Reflection
I learned how the staging area works and how to control exactly which files go into each commit. This matters because it helps commits stay organized and focused, making debugging and collaboration much easier.

## Checkpoint 2
### Commands
```
git log --oneline
git revert 6ca467b
git push
```
### Reflection
I learned how to undo a bad commit without removing it from history by using git revert. This matters because it preserves the project history while safely reversing unwanted changes, which is important when working in a collaborative environment.

## Checkpoint 3
### Commands
```
git checkout main
git add src/validator.py
git commit -m "Add is_positive helper function"
git log --oneline
git reset --hard HEAD~1
git checkout feature/mnguye31
git cherry-pick fc1fa90
git add src/validator.py
git cherry-pick --continue
git checkout main
git log --oneline
git checkout feature/mnguye31
git push
```
### Reflection
I learned how to move a commit from the wrong branch to the correct branch using git cherry-pick. I also learned how to resolve merge conflicts by keeping both the existing code and the incoming change, which is important when working with branches that modify the same file.

## Checkpoint 4
### Commands
```
git checkout -b experiment/mnguye31
git add src/calculator.py
git commit -m "Add checkpoint 4 comment"
git switch feature/mnguye31
git branch -D experiment/mnguye31
git reflog
git branch recovered/mnguye31 2277d4e
git merge recovered/mnguye31
git push
```
### Reflection
I learned how to recover lost work using git reflog after deleting a branch. This matters because it allows developers to retrieve commits that are no longer referenced by any branch, preventing accidental data loss.

## Checkpoint 6
### Commands
```
git log main..HEAD --oneline
git rebase -i main
git push --force-with-lease
git log --oneline
```
### Reflection
I learned how to use interactive rebase to clean up the commit history by changing vague commit messages into more descriptive ones. This matters because a clean and readable history makes it easier for teammates and reviewers to understand what was changed and why.