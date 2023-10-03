from PIL import Image, ImageFont, ImageDraw
import linecache
import random
import sys
import os
import git # script that contains my authentication

class GithubBannerGenerator:
    def __init__(self):
        self.phrase = ""
        self.ethan_git = git.EthanGit()

    def generate_nonsense_statement(self):
        # Since it is not cached anyways and one time use,
        # there is little benefit of caching this for more
        # efficiency, rather than counting it each time.

        try:

            with open('Data/statement/goofs.txt') as goofs, \
                 open('Data/statement/nouns.txt') as nouns, \
                 open('Data/statement/verbs.txt') as verbs, \
                 open('Data/statement/objects.txt') as objects:
                goofs_Lines = sum(1 for line in goofs)
                nouns_Lines = sum(1 for line in nouns)
                verbs_Lines = sum(1 for line in verbs)
                objects_Lines = sum(1 for line in objects)

                goofy_word = linecache.getline('Data/statement/goofs.txt', random.randint(0, goofs_Lines)).rstrip('\n')
                noun_word = linecache.getline('Data/statement/nouns.txt', random.randint(0, nouns_Lines)).rstrip('\n')
                verb_word = linecache.getline('Data/statement/verbs.txt', random.randint(0, verbs_Lines)).rstrip('\n')
                object_word = linecache.getline('Data/statement/objects.txt', random.randint(0, objects_Lines)).rstrip('\n')

                self.phrase = (goofy_word + " " + noun_word + " " + verb_word + " " + object_word)
                print("Phrase was updated via: statement")

        except IOError as e:
            # Should not happen
            print("Phrase was updated via: file error", e)
            pass

        return self.phrase

    def generate_nonsense_question(self):
        # To do...
        return self.phrase

    def generate_nonsense_fact(self):
        # To do...
        return self.phrase


    def create_banner(self, phrase):
        if not phrase:
            print("Failed to create new banner: no phrase")
            return None

        try:
            banner_empty_local_img = Image.open('Images/emptyGithubBanner.png')
            image_draw = ImageDraw.Draw(banner_empty_local_img)
            image_font = ImageFont.truetype('Fonts/CascadiaCode.ttf', 25)

            image_draw.text((90, 200), phrase, fill=(242, 243, 244), font=image_font)
            banner_empty_local_img.show()

            print("New banner image was created")

            banner_empty_local_img.save("Images/filledGithubBanner.png")

            with open("Images/filledGithubBanner.png", "rb") as image:
                image_data = bytearray(image.read())

            return bytes(image_data)
        except:
            print("Failed to create new banner: file path error")
            return None

    def update_github_banner(self, content):
        if not content:
            print("Banner failed to update: content is null")
            return

        file_to_push = self.ethan_git.ethan_github_repo.get_contents(self.ethan_git.ethan_banner_path)

        # Although it is ugly, (since I am unsure of the exact error via pyGithub)
        # this will do, it basically will try updating it first, then if that fails
        # try creating it, but if that fails, there is a internet issue or something
        try:
            contents = self.ethan_git.ethan_github_repo.get_contents(self.ethan_git.ethan_banner_path, ref="main")
            self.ethan_git.ethan_github_repo.update_file(self.ethan_git.ethan_banner_path, "Python: " + self.phrase, content=content, sha=contents.sha, branch="main")
            print("Banner updated successfully")
        except:
            try:
                self.ethan_git.ethan_github_repo.create_file(self.ethan_git.ethan_banner_path, "Python: " + self.phrase, content=content, branch="main")
            except:
                print("Banner failed to update: connection issue")
                return

    def generate_new_github_banner(self):
        # Randomly select one of the random phrase generators and then apply that
        # but here I only have one completed, so I will directly use it here
        print("Github banner generator method called")
        self.update_github_banner(self.create_banner(self.generate_nonsense_statement()))


banner = GithubBannerGenerator()
banner.generate_new_github_banner()