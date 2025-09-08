#main repo
#exercise-folder
#.\python-exercises



import pathlib , os

dir = pathlib.Path(r'.\python-exercises')

[file.unlink() for file in dir.iterdir()]

    

