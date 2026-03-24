- Checkpoint 1:
  - Task 1:
      git add test_calculator.py
      git commit -m “fix”
  - Task 2:
    git add validator.py
    git commit -m “update”
  git push origin feature/baotram5
  
This checkpoint gave me practice on committing my changes to my branch.

- Checkpoint 2:
  git log –oneline
  git revert b19f233
  git status
  git log –oneline
  git push origin feature/baotram5

This checkpoint let me understand how revert works and how I can change the effect of previous commits. It also gave me some experience with vim as well since I never really used it before.

Checkpoint 3:
  git switch main
  git status
  git add validator.py
  git –m commit "Add is_positive helper function"
  git log –oneline
  git reset –hard HEAD~1
  git switch feature/baotram5
  git cherry-pick db51f8b
  git log –oneline
  git switch main
  git log –oneline
  git push origin feature/baotram5

Checkpoint 4:
  git checkout -b experiment/baotram5
  git add calculator.py
  git commit -m “added test comment”
  git switch feature/baotram5
  git status
  git branch -D experiment/baotram5
  git reflog
  git branch recovered/baotram5 a221355
  git status 
  git merge recovered/baotram5
  git push origin feature/baotram5

Checkpoint 6:
  git log main..HEAD --oneline
  git rebase -i main
  git add calculator.py
  git commit —-amend
  git rebase —-continue
  git push –force-with-lease
