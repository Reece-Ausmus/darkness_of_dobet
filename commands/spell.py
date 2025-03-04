import requests

def spell_command(spell: str):
    base_url = "https://www.dnd5eapi.co/api/spells/"
    formatted_name = spell.lower().replace(' ', '-')
    api_url = f"{base_url}{formatted_name}"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        spell_data = response.json()
        return format_spell_data(spell_data)
    elif response.status_code == 404:
        return "Spell not found. Please check the spell name."
    else:
        return f"An error occurred: {response.status_code}"

def format_spell_data(data):
    # Extracting key information
    name = data.get('name', 'Unknown')
    level = data.get('level', 0)
    school = data.get('school', {}).get('name', 'Unknown School')
    casting_time = data.get('casting_time', 'Unknown')
    duration = data.get('duration', 'Unknown')
    range_ = data.get('range', 'Unknown')
    components = ', '.join(data.get('components', []))
    materials = data.get('material', '')
    description = "\n".join(data.get('desc', []))
    higher_level = "\n".join(data.get('higher_level', []))
    
    # Format for Discord
    spell_info = f"""**{name}**
Level: {level} | School: {school}
Casting Time: {casting_time}
Range: {range_}
Duration: {duration}
Components: {components} {'('+materials+')' if materials else ''}

**Description:**
{description}
"""
    if higher_level:
        spell_info += f"\n**At Higher Levels:**\n{higher_level}"

    return spell_info

def spell_usage():
    return "⚠️ Format your spell lookup like `!spell fireball`"