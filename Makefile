# Règle par défaut 'all' pour exécuter le clean et le script Python
all: clean run_python

# Définit la règle pour 'clean'
clean:
	@echo "Suppression des fichiers .sh et .json..."
	@rm -f *.sh *.json

# Définit la règle pour exécuter le script Python
run_python:
	@echo "Exécution du script render_and_generate_bash.py..."
	@python3 render_and_generate_bash.py
	@chmod 770 *.sh
