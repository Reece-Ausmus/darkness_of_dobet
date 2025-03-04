import random

def roll_command(dice):
    response = "```"
    total_sum = 0
    for die in dice:
        try:
            if die[-1] in ['+', '-']:
                num, sides = map(int, die[:-1].lower().split('d'))
                roll_ad = 1 if die[-1] == '+' else -1
            else:
                num, sides = map(int, die.lower().split('d'))
                roll_ad = 0

            if roll_ad == 1: # Advantage
                rolls = [(random.randint(1, sides), random.randint(1, sides)) for _ in range(num)]
                final_rolls = [max(roll) for roll in rolls]
            elif roll_ad == -1: # Disadvantage
                rolls = [(random.randint(1, sides), random.randint(1, sides)) for _ in range(num)]
                final_rolls = [min(roll) for roll in rolls]
            else:
                rolls = [random.randint(1, sides) for _ in range(num)]
                final_rolls = rolls

            advantage_text = 'with advantage' if roll_ad == 1 else 'with disadvantage' if roll_ad == -1 else ''
            die_chunk = f"{num}d{sides}:"
            if roll_ad != 0:
                rolls_chunk = "[" + ', '.join(f"({r1},{r2})" for r1, r2 in rolls) + "]" + f" {advantage_text}"
            else:
                rolls_chunk = "[" + ','.join(map(str, rolls)) + "]" + f" {advantage_text}"
            response += f"{die_chunk}" + " "*(7-len(die_chunk))
            response += f"{rolls_chunk}\n"
            total_sum += sum(final_rolls)
        except ValueError:
            return roll_usage()
    response += f"Total: {total_sum}```"
    return response
        
def roll_usage():
    return "⚠️ Format your roll like `!roll 2d20`"