from db_handler import get_initiative
import random


def initiative_command(args):
    response = get_initiative()
    if response:
        char_naming = 1
        for arg in args:
            try:
                if arg[-1] in ['+', '-']:
                    count, initiative = map(int, arg[:-1].split('x'))
                    initiative_ad = 1 if arg[-1] == '+' else -1
                else:
                    count, initiative = map(int, arg.split('x'))
                    initiative_ad = 0
                for _ in range(count):
                    response.append({'name': f'Character {char_naming}', 'initiative': initiative, 'initiative_ad': initiative_ad})
                    char_naming += 1
            except ValueError:
                return initative_usage()
        return format_initiative_data(response)
    else:
        return "No characters found in the database."
    

def format_initiative_data(data):
    for character in data:
        if character['initiative_ad'] == 1: # Advantage
            roll1 = random.randint(1, 20)
            roll2 = random.randint(1, 20)
            character['initiative_roll'] = max(roll1, roll2) + character['initiative']
            character['rolls'] = (roll1, roll2)
        elif character['initiative_ad'] == -1: # Disadvantage
            roll1 = random.randint(1, 20)
            roll2 = random.randint(1, 20)
            character['initiative_roll'] = min(roll1, roll2) + character['initiative']
            character['rolls'] = (roll1, roll2)
        else:
            roll = random.randint(1, 20)
            character['initiative_roll'] = roll + character['initiative']
            character['rolls'] = (roll,)
    
    sorted_data = sorted(data, key=lambda x: (x['initiative_roll'], max(x['rolls'])), reverse=True)
    formatted_data = "```"
    for character in sorted_data:
        rolls = ', '.join(map(str, character['rolls']))
        advantage_text = 'with advantage' if character['initiative_ad'] == 1 else 'with disadvantage' if character['initiative_ad'] == -1 else ''
        name_chunk = f"{character['name']}: "
        initiative_chunk = f"{character['initiative_roll']}"
        rolled_chunk = f"Rolled: ["
        if character['initiative_ad'] != 0:
            rolled_chunk += f"({rolls})"
        else:
            rolled_chunk += rolls
        rolled_chunk += f"] {advantage_text}"
        bonus_chunk = f"Bonus: (+{character['initiative']})"
        formatted_data += name_chunk + " "*(14-len(name_chunk))
        formatted_data += initiative_chunk + " "*(7-len(initiative_chunk))
        formatted_data += rolled_chunk + " "*(38-len(rolled_chunk))
        formatted_data += bonus_chunk + "\n"
    formatted_data += "```"
    return formatted_data

def initative_usage():
    return "⚠️ Format your initiative roll like `!initiative 1x4 2x6 1x8`"