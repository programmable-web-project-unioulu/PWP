# Basic steps to contribute
If there are some files you wish to not include in push (any secrets, etc...), add them to .gitignore file, else add the files one by one with ```git add filename```
After you are ready to push the files
```console
git add .
OR
git add <filename> <filename> <filename>
OR
git commit . -m "reasonable commit message, e.g. Initial database tests"

# Create new branch locally and change to it
git checkout -b <branch name> 
# Push the changes to own branch
git push origin <branch name>

1. Create a pull request to master
2. Wait for approval
3. Violently demand approval in discord
4. Apply changes to code, if any
5. Merge

```

If conflict in branch, e.g. something changed in master prior merge

```
# In local environment, in own branch
git pull master --rebase
# resolve conflicts in VSCode, protip: in VSCode in file with conflicts CTRL+P Accept all incoming, use wisely
# After resolving conflicts commit
git commit --amend --no-edit
git push origin <your branch> --force-with-lease
# Check in github if no conflicts
Merge 
```