import enum


class Prompts(enum.Enum):
    GIT_COMMAND_PROMPT = """
    ### Git Command Translation ###
    Translate the given statements into corresponding Git commands. You have a list of Git commands to choose from:
    
    - `git init`: Initialize a local Git repository.
    - `git clone [url]`: Create a local copy of a remote repository.
    - `git status`: Check the repository's status.
    - `git add [file]`: Add a file to the staging area.
    - `git commit -m "[message]"`: Commit changes with a message.
    - `git rm -r [file]`: Remove a file or folder.
    - `git branch`: List local branches.
    - `git push origin --delete [branch]`: Delete a remote branch.
    - `git checkout -b [branch]`: Create and switch to a new branch.
    - `git branch -m [old] [new]`: Rename a local branch.
    - `git merge [branch]`: Merge a branch into the active branch.
    - `git stash`: Stash changes in the working directory.
    - `git pull`: Update the local repository.
    - `git remote add origin [url]`: Add a remote repository.
    - `git remote set-url origin [url]`: Set the remote repository's URL.
    - `git log`: View commit history.
    - `git diff [source] [target]`: Preview changes before merging.
    
    Provide the Git commands for the following statements:
    
    Q: initialize the repository. then save the hello-world.com url as origin.
    A: git init && git remote add origin hello-world.com
    
    Q: add the main.py file to git and list the files added to git.
    A: git add main.py & git status
    
    Q: switch to x branch. if there is no branch, create an x branch.
    A: git checkout -b x
    
    Q: {question}
    A: Lets think about step by step: 
"""
