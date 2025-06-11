all:
	docker build -t finance-tracker .
	docker run -p 8000:8000 finance-tracker

.PHONY: docker push
	docker build -t finance-tracker .
	docker tag finance-tracker:latest yourdockerhubusername/finance-tracker:latest
	docker push yourdockerhubusername/finance-tracker:latest

clean:
	docker rmi finance-tracker
	docker rmi yourdockerhubusername/finance-tracker:latest || true
	docker system prune -f
	
.PHONY: clean
.PHONY: all
.PHONY: run
run:
	docker run -p 8000:8000 finance-tracker

.PHONY: push
push:
	git add .
	git commit -m "Update Dockerfile and Makefile"
	git push origin main
.PHONY: deploy
deploy:
	ssh user@yourserver "cd /path/to/your/app && git pull && docker-compose up -d --build"

.PHONY: deploy
.PHONY: test
test:
	docker run --rm finance-tracker pytest tests/
.PHONY: test
.PHONY: lint
lint:
	docker run --rm -v $(pwd):/app finance-tracker flake8 /app
.PHONY: lint
.PHONY: format
format:
	docker run --rm -v $(pwd):/app finance-tracker black /app
.PHONY: format
.PHONY: shell
shell:
	docker run -it --rm -v $(pwd):/app finance-tracker /bin/bash
.PHONY: shell
.PHONY: help
help:
	@echo "Makefile commands:"
	@echo "  all       - Build and run the Docker container"
	@echo "  build     - Build the Docker image"
	@echo "  push      - Push the Docker image to Docker Hub"
	@echo "  clean     - Remove Docker images and prune system"
	@echo "  run       - Run the Docker container"
	@echo "  deploy    - Deploy the application to a remote server"
	@echo "  test      - Run tests using pytest"
	@echo "  lint      - Run flake8 for code linting"
	@echo "  format    - Format code using black"
	@echo "  shell     - Open a shell in the Docker container"