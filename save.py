from os import system
progress = input("Briefly explain your progress: ")
for command in 'git stage *;git commit -m "progress";git push'.split(","):
    command = command.replace("progress", progress)
    system(command)