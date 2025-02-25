PASTA_AMBIENTE_VIRTUAL = .venv
REQUIREMENTS = requirements.txt
TESTES_UNITARIOS_REQUIREMENTS = requirements_unit_test.txt

env:
	clear
	@echo "Removendo ambiente virtual $(PASTA_AMBIENTE_VIRTUAL) caso exista..."
	rm -rf $(PASTA_AMBIENTE_VIRTUAL)
	@echo

	@echo "Gerando novo ambiente virtual: $(PASTA_AMBIENTE_VIRTUAL)"
	python3 -m venv $(PASTA_AMBIENTE_VIRTUAL)
	@echo

	@echo "Instalando dependências..."
	@if [ -f "$(REQUIREMENTS)" ]; then \
		echo "Instalando arquivo $(REQUIREMENTS)"; \
		$(PASTA_AMBIENTE_VIRTUAL)/bin/pip install -r $(REQUIREMENTS); \
	fi

	@if [ -f "$(TESTES_UNITARIOS_REQUIREMENTS)" ]; then \
		echo "Instalando arquivo $(TESTES_UNITARIOS_REQUIREMENTS)"; \
		$(PASTA_AMBIENTE_VIRTUAL)/bin/pip install -r $(TESTES_UNITARIOS_REQUIREMENTS); \
	fi

	@echo "======================================================="
	@echo "Criação e instalação do ambiente virtual concluído..."
	@echo "======================================================="
	@echo "Para ativar o ambiente execute o comando source "$(PASTA_AMBIENTE_VIRTUAL)"/bin/activate"
