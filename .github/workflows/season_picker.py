import re
import datetime
import random

MAX_SUMMER_IMAGES = 4
MAX_AUTUMN_IMAGES = 4
MAX_WINTER_IMAGES = 3
MAX_SPRING_IMAGES = 3


class SeasonStemCreator:
    def __init__(self):
        now = datetime.datetime.now()

        if (3, 21) <= (now.month, now.day) < (6, 21):
            self.season = '_autumn'
            self.max_images = MAX_AUTUMN_IMAGES
        elif (6, 21) <= (now.month, now.day) < (9, 21):
            self.season = '_winter'
            self.max_images = MAX_WINTER_IMAGES
        elif (9, 21) <= (now.month, now.day) < (12, 21):
            self.season = '_spring'
            self.max_images = MAX_SPRING_IMAGES
        else:
            self.season = '_summer'
            self.max_images = MAX_SUMMER_IMAGES

    def generate_rand_stem(self):
        return self.season + str(random.randint(1, self.max_images)) + '.gif'


def get_current_season_gifname():
    season_stem_creator = SeasonStemCreator()
    return season_stem_creator.generate_rand_stem()


def update_gif():

    with open('README.md', 'r') as readme_file:
        readme_content = readme_file.read()

    tag_id = 'season'

    current_season = get_current_season_gifname()
    new_src = 'https://raw.githubusercontent.com/MiguelV5/MiguelV5/main/misc/' + current_season

    pattern = r'<img.*?id="{}".*?src=".*?"'.format(tag_id)
    replacement = '<img id="{}" height=210 src="{}"'.format(tag_id, new_src)
    updated_content = re.sub(pattern, replacement,
                             readme_content, flags=re.IGNORECASE)

    with open('README.md', 'w') as readme_file:
        readme_file.write(updated_content)


if __name__ == '__main__':
    update_gif()
