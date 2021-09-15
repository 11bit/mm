venv-activate:
	source env/bin/activate
ttx:
	ttx -d ./api/fonts/otf font-sources/otf/*.otf
	ttx -d ./api/fonts/ttf font-sources/ttf/*.ttf