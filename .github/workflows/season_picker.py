import re
import datetime

MAX_SUMMER_IMAGES = 4
MAX_AUTUMN_IMAGES = 4
MAX_WINTER_IMAGES = 3
MAX_SPRING_IMAGES = 3
MAIN_MISC_PATH = 'https://raw.githubusercontent.com/MiguelV5/MiguelV5/main/misc/'


class SeasonStemCreator:

    def _get_new_image_number(self, prev_readme_content):

        tag_id = 'season'
        pattern = r'<img.*?id="{}".*?src="{}(?P<number>[0-9]+)\.gif"'.format(
            tag_id, MAIN_MISC_PATH
        )
        match = re.search(pattern, prev_readme_content, flags=re.IGNORECASE)

        if match:
            previous_image_number = int(match.group('number'))
        else:
            previous_image_number = 1  # Default value

        new_image_number = (previous_image_number % self.max_images) + 1

        return new_image_number

    def __init__(self, prev_readme_content):
        now = datetime.datetime.now()

        if (3, 21) <= (now.month, now.day) < (6, 20):
            self.season = '_autumn'
            self.max_images = MAX_AUTUMN_IMAGES
        elif (6, 21) <= (now.month, now.day) < (9, 20):
            self.season = '_winter'
            self.max_images = MAX_WINTER_IMAGES
        elif (9, 21) <= (now.month, now.day) < (12, 20):
            self.season = '_spring'
            self.max_images = MAX_SPRING_IMAGES
        else:
            self.season = '_summer'
            self.max_images = MAX_SUMMER_IMAGES

        self.new_image_number = self._get_new_image_number(prev_readme_content)

    def generate_new_stem(self):
        return self.season + str(self.new_image_number) + '.gif'


def get_current_season_gifname(prev_readme_content):
    season_stem_creator = SeasonStemCreator(prev_readme_content)
    return season_stem_creator.generate_new_stem()


def update_gif():
    with open('README.md', 'r') as readme_file:
        prev_readme_content = readme_file.read()

    tag_id = 'season'

    current_season = get_current_season_gifname(prev_readme_content)
    new_src = MAIN_MISC_PATH + current_season

    pattern = r'<img.*?id="{}".*?src=".*?"'.format(tag_id)
    replacement = '<img id="{}" height=210 src="{}"'.format(tag_id, new_src)
    updated_content = re.sub(pattern, replacement,
                             prev_readme_content, flags=re.IGNORECASE)

    with open('README.md', 'w') as readme_file:
        readme_file.write(updated_content)


if __name__ == '__main__':
    update_gif()
