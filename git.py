from github import Github

class EthanGit:
    def __init__(self):
        print("EthanNGit starting")
        self.ethan_github = Github("EthanNgit", "auth_token")
        self.ethan_github_repo = self.ethan_github.get_user().get_repo("EthanNgit")
        self.ethan_banner_path = "filledGithubBanner.png"
        print("EthanNGit initialized")
