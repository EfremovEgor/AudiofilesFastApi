run-db:
	docker run --name postgres_db -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_DB=db -v ${PWD}/db_data:/var/lib/postgresql/data  -d postgres
