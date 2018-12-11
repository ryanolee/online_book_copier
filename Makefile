build:
	@docker build . --rm --tag=ghostpy:latest

run: 
	@docker run --mount src=`pwd`/chap,target=/app/chap,type=bind ghostpy:latest  python3 /app/main.py 