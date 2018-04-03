```bash
rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex (master)
$ git config -l | grep "^remote\."
remote.origin.url=https://gitlab.com/hygull/pylatex.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex (master)
$ git remote set-url --add --push origin "https://github.com/hygull/pylatex.git"

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex (master)
$ git config -l | grep "^remote\."
remote.origin.url=https://gitlab.com/hygull/pylatex.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
remote.origin.pushurl=https://github.com/hygull/pylatex.git

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex (master)
$ git remote set-url --add --push origin "https://gitlab.com/hygull/pylatex.git"

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex (master)
$ git config -l | grep "^remote\."
remote.origin.url=https://gitlab.com/hygull/pylatex.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
remote.origin.pushurl=https://github.com/hygull/pylatex.git
remote.origin.pushurl=https://gitlab.com/hygull/pylatex.git

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex (master)
$
```