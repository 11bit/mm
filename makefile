venv-activate:
	source env/bin/activate

clean:
	rm -f ./api/fonts/otf/*.ttx
	rm -f ./api/fonts/ttf/*.ttx

ttx:
	make clean
	ttx -d ./api/fonts/otf font-sources/otf/*.otf
	ttx -d ./api/fonts/ttf font-sources/ttf/*.ttf