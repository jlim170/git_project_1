## Checkpoint 1:

git add tests/test_calculator.py
git commit -m "fix"

git add src/calculator.py
git commit -m "update"

git push origin feature/joslim23

I learned how to stage changes, commit changes, and push these commits to the remote branch to update my code changes in GitHub.

## Checkpoint 2:

git log --oneline

git revert 66f6716

git commit --amend -m "Remove the excessive debug logging in the calculator module by reverting the commit with those changes while keeping the commit in history"
(I forgot to modify the default comment for the revert so using amend here)

git push origin feature/joslim23

I learned how to undo the effects of a commit without removing it from history in case I am ever in this scenario.

## Checkpoint 3:

git switch main

git add src/validator.py

git commit -m "Add is_positive helper function"

git log --oneline

git reset --hard HEAD~1

git switch feature/joslim23

git cherry-pick 4d9857d

git status

git add src/validator.py

git cherry-pick --continue

git log --oneline

git switch main

git log --oneline

git switch feature/joslim23

git push origin feature/joslim23

I learned how to move a commit from a wrong branch to the correct branch in case I accidentally commit to a wrong branch. I also learned how to handle merge conflicts in case there is conflicting code that you need to merge.

## Checkpoint 4:

git checkout -b experiment/joslim23

git add src/validator.py

git commit -m "Added a comment to src/validator.py"

git switch feature/joslim23

git branch -D experiment/joslim23

git switch -c recovered/joslim23 7cacc5c

git switch feature/joslim23

git merge recovered/joslim23

git log --oneline

git push origin feature/joslim23

I learned how to recover lost commits from a deleted branch that weren’t merged. This will help if you accidentally delete a branch before merging it.

## Checkpoint 5:

git remote add upstream https://github.com/mdurrani808/git_project_1.git

git remote -v

git fetch upstream

git switch main

git merge upstream/main

git switch feature/joslim23

git rebase main

git push --force-with-lease origin feature/joslim23

I learned how to rebase my feature branch with the latest upstream main branch. This matters since I learned how to add the changes from an upstream repository’s main branch to my current feature branch.

## Checkpoint 6:

git log main..HEAD --oneline

git rebase -i main

git log --oneline 

git push --force-with-lease

I learned how to clean up the history of my commits by running an interactive rebase by using settings like reword and squash. This matters since now I can make the commits tell a clear story of my work.