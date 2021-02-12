# my_repo_files
pull
push
clone
commit
add
branch
status
worktree(creatig branch)


=========================
Login to Github in URL

Select repo https://github.com/pmuthubalu?tab=repositories and copy repo URL

https://github.com/pmuthubalu/my_repo_files

To Run Foolowing command to clone

muthu@muthu-vbox:~/my_repo_files$ git clone https://github.com/pmuthubalu/my_repo_files.git

muthu@muthu-vbox:~/my_repo_files$ cd my_repo_files/

muthu@muthu-vbox:~/my_repo_files$ ls
README.md  remove.sh  

muthu@muthu-vbox:~/my_repo_files$ vim sum1.py

muthu@muthu-vbox:~/my_repo_files$ ls
README.md  remove.sh  sum1.py

muthu@muthu-vbox:~/my_repo_files$ python3 sum1.py 
PRG=1
6
#######

PRG=2
3
6
#######

PRG=3
muthu@muthu-vbox:~/my_repo_files$ clear

muthu@muthu-vbox:~/my_repo_files$ git add sum1.py
muthu@muthu-vbox:~/my_repo_files$ ls
README.md  remove.sh  sum1.py

muthu@muthu-vbox:~/my_repo_files$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   sum1.py

muthu@muthu-vbox:~/my_repo_files$ git commit
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'muthu@muthu-vbox.(none)')

muthu@muthu-vbox:~/my_repo_files$ git config --global user.email p.muthubalu@gmail.com
muthu@muthu-vbox:~/my_repo_files$ git config --global user.name Muthukumar

muthu@muthu-vbox:~/my_repo_files$ git commit
Use "fg" to return to nano.or to close the file... 

[1]+  Stopped                 git commit

muthu@muthu-vbox:~/my_repo_files$ git commit -m "sum of the elements in list"
[main 2a904f6] sum of the elements in list
 1 file changed, 20 insertions(+)
 create mode 100644 sum1.py
 
muthu@muthu-vbox:~/my_repo_files$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

muthu@muthu-vbox:~/my_repo_files$ git push
Username for 'https://github.com': p.muthubalu@gmail.com
Password for 'https://p.muthubalu@gmail.com@github.com': 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 442 bytes | 442.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/pmuthubalu/my_repo_files.git
   836c96b..2a904f6  main -> main
   
muthu@muthu-vbox:~/my_repo_files$


