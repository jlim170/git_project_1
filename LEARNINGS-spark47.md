## Checkpoint 1: Fixing Dividing by Zero
**Git Commands:**
- git branch
- git add src/calculator.py
- git commit -m "fix"
- git add src/validator.py
- git commit -m "update"
- git push origin feature/spark47

**What I learned:**
I learned how to write a test that expects a specific exception (divide-by-zero). I also learned how to write a module-level docstring to explain the purpose of a file. I also learned how to write DEBUG statements.


## Checkpoint 2: Revert BAD commit
**Git Commands:**
- git log --oneline
- git revert 4dc20fb
- Had a merge conflict so needed to fix that and update the file again
- git add src/calculator.py
- git revert --continue
- git push origin feature/spark47

**What I learned:**  
I learned how to undo a commit using `git revert` without removing it from history, how to resolve merge conflicts safely, and how to preserve my own changes while removing unwanted debug code.


## Checkpoint 3: Moving a commit to the right branch
**Git commands:**
- git checkout main
- git branch #checking branch
- git add src/validator.py
- git commit -m "Add is_positive helper function"
- git log --oneline #noted commit hash
- git reset --hard HEAD~1
- git log --oneline #check that it is gone
- git checkout feature/spark47
- git branch
- git cherry-pick 47808c1 #resolved some merge conflicts
- git add src/validator.py
- git cherry-pick --continue
- git log --oneline #check it was added to my branch
- git checkout main
- git log --oneline #check it was removed here

**What I learned:**
I learned how to move a commit from the wrong branch to the correct branch using 
`git cherry-pick`, how to reset a branch safely with `git reset --hard`, 
and how to resolve conflicts to keep both sets of changes.


## Checkpoint 4: Recovering lost work with reflog
**Git commands:**
- git checkout -b experiment/spark47
- git add .
- git commit -m "Experiment: add temp comment"
- git checkout feature/spark47
- git branch -D experiment/spark47
- git reflog #Find lost commit and hash
- git checkout -b recovered/spark47 de0d418
- git checkout feature/spark47
- git merge recovered/spark47
- git log --oneline #Check history

**What I learned:**  
I learned that even if a branch is deleted, its commits can still be recovered using `git reflog`. I can also restore lost work by creating a new branch from a previous commit and merging it back.


## Checkpoint 6: Interactive rebase to clean up history
**Git commands:**
- git log main..HEAD --oneline
- git rebase -i main
- git push --force-with-lease

**What I learned:**  
I learned how to use interactive rebase to clean up commit history by renaming unclear commit messages. I also learned how to safely update a remote branch after rewriting history using `git push --force-with-lease`.