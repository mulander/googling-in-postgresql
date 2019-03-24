all: table load index

table:
	psql -U postgres -f table.sql

load:
	python3.6 load.py

index:
	psql -U postgres -f index.sql

