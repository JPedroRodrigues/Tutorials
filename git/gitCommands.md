# Today we're going to get in touch with some useful git commands

- Hope you enjooooy it! ₍ᐢ•`ᴥ´•ᐢ₎
- Puppy's reference: https://git-scm.com/docs/gittutorial

---

### Topics
- [Getting Started](#getting-started)
- [Project History](#project-history)
- []

---

# Getting Started

- Introduce yourself to git

```git
git config --global user.name "my username"
```
```git
git config --global user.email user@email.com
```

- Get some help (e.g. log command)

```git
man git-log
```

```git
git help log
```

- Initialize a repository

```git
git init
```
- Getting git to know the contents of all files under the current directory
	- Stores data into an "index" area (add them to index)

```git
git add .
```

- By modifying some files, you can add them to the index as shown below

```git
git add file1.txt file2.txt file3.txt
```

- Commit

```git
git commit -m "commit message"
```

- Commit with git add
	- Uses automatically git add, identifying any modified (but not new) files

```git
git commit -a
```

- Check what is about to be committed
	- --cached will show what was added to the index

```git
git diff --cached
```

- Push

```git
git push
```

# PROJECT HISTORY

- View the history of changes

```git
git log
```

- You can also check the diffs at each step

```git
git log -p
```

- Getting some overview

```git
git log --stat --summary
```

# BRANCHES

- Create branch locally

```git
git branch <branch name>
```

- Publish branch remotely

```git
git push origin -u <branch name>
```

- Delete branch locally

```git
git branch -D <branch name>
```

- Delete branch remotely

```git
git push origin -d <branch name>
```

- Change current branch

```git
git checkout <branch name>
```

- You can also switch between branches by using

```git
git switch <branch name>
```

- Show remote and local branches

```git
git branch -al
```

- Verify branch status

```git
git status
```

- Merge branch

```git
git merge <branch name>
```

- If something goes wrong while merging, you can see the conflicts using

```git
git diff
```

- Graphical representation of the resulting history

```git
gitk
```

# GIT & COLLABORATION

- Cloning a repo locally 

```git
git clone path/path/projectPath
```

- Pull from a repo locally
	- Merges changes from friend's repo to your master
	- Fetches changes from a remote branch, then merges into the current branch

```git
git pull home/friendProject/hisRepo master
```

- Peek what your work partner did
	- Uses FETCH_HEAD to check if the other branch has anything worth pulling
	- HEAD..FETCH_HEAD says to show everything that is reachable from the FETCH_HEAD
	(other branch's state) but exclude anything that is reachable from HEAD (current branch's state).

```git
git fetch home/friendProject/hisRepo master
```

```git
git log -p HEAD..FETCH_HEAD
```

- Check what someone done since branches forked

```git
gitk HEAD..FETCH_HEAD
```

- Check what you did too since both branches forked (three dots)

```git
gitk HEAD...FETCH_HEAD
```

- Interact with other repos and add them (creating a new remote called "friend")

```git
git remote add friend home/friendProject/hisRepo
```

- First part of pull operation: fetching

```git
git fetch friend
```

- Showing list of all changes our friend made after branching from our master

```git
git log -p master..friend/master
```

- Now you coudl merge or merging by pulling

```git
git merge friend/master
```

```git
git pull . remotes/friend/master
```

- Our friend could easily pull our changes
	- Because, by cloning our repo, git already stores its location

```git
git pull
```

- Taking a look at the configuration made by git clone

```git
git config -l
```

- Checking the copy of our repo's master under the name origin/master

```git
git branch -r
```

- Performing clones and pulls using the ssh protocol

```git
git clone someone.org:home/someone/project myrepo
```

# EXPLORING HISTORY

- Showing some commit or the most recent of a branch

```git
git show <first few character of a commits' name or the full name of a branch>
```

- Looking at the previous commit of the one you listed

```git
git show HEAD^  	(check HEAD's parent)
git show HEAD^^		(check HEAD's grandparent)
git show HEAD~4  	(check HEAD's great-great grandparent of HEAD)
```

- Our commit may have more than one parent, who knows

```git
git show HEAD^1  	(show the first parent of HEAD such as HEAD^)
git show HEAD^2  	(show the second parent of HEAD)
```

- You can name a commit

```git
git tag <name of your choice> <first few characters of a commit's name>
```

e.g.: `git tag v2.5 1b2e1d63ff`

- Compare two different commits

```git
git diff <commit's tag/name> <other commit's tag/name>
```

- Creating a new branch based on a commit 

```git
git branch <new branch's name> <commit's tag/name>
```

- Resets a branch based on a previous state
	- Be careful using this lil command right here as it will force other devs
	- to pull and make new merges. Also, it deletes your subsequent commits
	- Try git revert to undo changes that you have pushed

```git
git reset --hard HEAD^
```

- Searching for strings in any version of our project

```git
git grep "<string>" <commit's tag/name>
```

```git
git grep "string" (git will use the current directory)
```

- Range your commits using git log

```git
git log v2.5..v2.6  		(commits between v2.5 and v2.6)
git log v2.5..  		(commits since v2.5)
git log --since="2 weeks ago"  	(commits from the last 2 weeks)
git log v2.5.. Makefile 	(commits since v2.5 which modify Makefile)
```

- You can list commits of divergent branches

```git
git log master..stable  (will list commits made in the master bit not in the stable branch)
```

```git
git log stable..master	(will list commits made in the stable but not in the master branch)
```

- You can always visualize thte differences with more accuracy using gitk

```git
gitk --since="2 weeks ago" <directory's name>
```

- Difference between two specific files from two diferrent versions

```git
git diff v2.5:Makefile HEAD:Makefile.in
```

- You can also use git show to see any such file

```git 
git show v2.5:Makefile
```