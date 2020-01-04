""""
a GitHub sorting using python and PyGithub
sources: https://pypi.org/project/PyGithub/
"""

# imports
from github import Github

def main():
    # enter access token or username and password as strings separated by a comma
    g = Github("some_access_token")

    # enter you username
    your_name = "your_username"

    repos = g.get_user(your_name).get_repos()

    # sorts public repos alphabetically and prints them
    reponames = sorted(repo.name for repo in repos)

    print(f"You have {len(reponames)} under your user.")
    print("The list of repositories is the following:")
    for name in reponames:
        print(name)


# system calls main
if __name__ == "__main__":
    main()
