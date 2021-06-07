"""Function collection for player data acquisition"""
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_player_data(url):
    """Collect player data and store it in data frames:
        Available lists:
        - Passing
        - Receiving
        - Rushing
        - Defense (per Player)
        - Kicking/Punting
    => Later: Combine lists to get sort data for each player"""
    lists = ["passing", "rushing", "receiving"]
    category_list_url = url + lists[0] + ".htm"
    data = scrap_category(category_list_url, cat)
    return data


def scrap_category(cat_url, cat):
    response = requests.get(cat_url)
    """Get html code of page"""
    html = BeautifulSoup(response.text, 'html.parser')
    """Find available players"""
    table = html.find_all('table')[0]
    player_list = []
    for row in table.find_all('tr'):
        # print(row)
        columns = row.find_all('td')
        player_name = 0
        player_team = 0
        player_position = 0
        player_url = 0
        # passing
        pass_attempts = 0
        pass_cmp = 0
        pass_yds = 0
        pass_td = 0
        pass_int = 0
        sacks = 0
        sack_loss = 0
        for element in columns:
            # print(element.get("data-stat"))
            # print(element.text)

            if element.get("data-stat") == "player":

                player_url = "https://www.pro-football-reference.com" + element.find("a").get('href')

            if element.get("data-stat") == "player":
                player_name = element.getText()
                """Remove award signs"""
                if "+" in player_name:
                    player_name = player_name[:-1]
                if "*" in player_name:
                    player_name = player_name[:-2]

            if element.get("data-stat") == "team":
                player_team = element.getText()

            if element.get("data-stat") == "pos":
                player_position = element.getText()

            if cat == 'passing':
                if element.get("data-stat") == "pass_att":
                    pass_attempts = element.getText()

                if element.get("data-stat") == "pass_cmp":
                    pass_cmp = element.getText()

                if element.get("data-stat") == "pass_yds":
                    pass_yds = element.getText()

                if element.get("data-stat") == "pass_td":
                    pass_td = element.getText()

                if element.get("data-stat") == "pass_int":
                    pass_int = element.getText()

                if element.get("data-stat") == "pass_sacked":
                    sacks = element.getText()

                if element.get("data-stat") == "pass_sacked_yds":
                    sack_loss = element.getText()

            player_dict = {"Name": player_name, "URL": player_url, "Position": player_position, "Team": player_team,
                           "Attempts": pass_attempts, "Completions": pass_cmp, "Pass yards": pass_yds, "Pass td": pass_td,
                           "Pass int":pass_int, "Sacks": sacks, "Sack loss yds": sack_loss}
        if player_name != 0:
            player_list.append(player_dict)
    frame = pd.DataFrame(player_list)
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #     print(frame)
    return frame

