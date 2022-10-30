""" branch-prefix hook to add a prefix to branch name when it doesn't have one
"""
from re import IGNORECASE, match

from git import Repo
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def check_branch_name():
    """ Rename branch to `[prefix][separator]branch_name` if branch_name is not in ignore list
    """
    with open('branch-prefix.yaml', encoding='UTF-8') as file:
        settings = load(file.read(), Loader=Loader)
    repo = Repo('.')
    active_branch = repo.active_branch.name

    if active_branch in settings['ignore-branches'] or \
       any( match(rf'^{pattern}', active_branch, IGNORECASE) for pattern in
            settings['ignore-branches-starting-with'] ):
        return

    new_branch_name = f"{settings['prefix']}{settings['separator']}{active_branch}"
    print(f"Current branch: '{active_branch}' does not contain a prefix,"
          f" renaming to {new_branch_name}.")
    repo.active_branch.rename(new_branch_name)
