import yaml
from jinja2 import Environment, FileSystemLoader

# Charger les variables à partir du fichier YAML
with open('switches.yml') as f:
    switches_data = yaml.safe_load(f)

# Configurer Jinja2 pour utiliser le répertoire contenant les templates
env = Environment(loader=FileSystemLoader('.'))

# Template pour les fichiers JSON des switchs
json_template = env.get_template('mqtt_switch_discovery_template.j2')

# Template pour le script Bash
bash_template = env.get_template('mqtt_publish_commands_template.j2')

# Générer les fichiers JSON pour chaque switch
for switch in switches_data['switches']:
    output_json = json_template.render(switches=[switch], has_discover_sw=switches_data['has_discover_sw'])
    json_filename = f"output_{switch['unique_id']}.json"
    with open(json_filename, 'w') as json_file:
        json_file.write(output_json)
    print(f"Fichier JSON généré : {json_filename}")

# Générer le script Bash pour publier tous les switchs
output_bash = bash_template.render(switches=switches_data['switches'], 
                                   has_discover_sw=switches_data['has_discover_sw'],
                                   mqtt_broker=switches_data.get('mqtt_broker', 'localhost'),
                                   mqtt_user=switches_data.get('mqtt_user', ''),
                                   mqtt_pass=switches_data.get('mqtt_pass', ''))

# Écrire le script Bash dans un fichier
bash_filename = "mqtt_publish_commands.sh"
with open(bash_filename, 'w') as bash_file:
    bash_file.write(output_bash)

print(f"Script Bash généré : {bash_filename}")

