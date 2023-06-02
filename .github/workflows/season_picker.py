import re
import datetime
import random

def get_current_season_gifname():
    now = datetime.datetime.now()
    month = now.month

    # Determine the current season based on the month
    if 3 <= month <= 5:
        if random.randint(1,2) == 1:
            return 'anasabdin_autumn.gif'
        else:
            return 'anasabdin_autumn2.gif'
    elif 6 <= month <= 8:
        return 'anasabdin_winter.gif'
    elif 9 <= month <= 11:
        return 'anasabdin_spring.gif'
    else:
        if random.randint(1,2) == 1:
            return 'anasabdin_summer.gif'
        else:
            return 'anasabdin_summer_night.gif'

        
def update_gif():
    # Read the README.md file
    with open('README.md', 'r') as readme_file:
        readme_content = readme_file.read()

    # Specify the HTML tag with the ID
    tag_id = 'season'

    # Get the current season
    current_season = get_current_season_gifname()
    new_src = 'https://raw.githubusercontent.com/MiguelV5/MiguelV5/main/misc/' + current_season
    
    # Find and replace the image source in the README.md content
    pattern = r'<img.*?id="{}".*?src=".*?"'.format(tag_id)
    replacement = '<img id="{}" src="{}"'.format(tag_id, new_src)
    updated_content = re.sub(pattern, replacement, readme_content, flags=re.IGNORECASE)

    # Write the updated content back to the README.md file
    with open('README.md', 'w') as readme_file:
        readme_file.write(updated_content)

if __name__ == '__main__':
    update_gif()
