IMAGE_NAME := adk-tw-forex
AGENTS_DIR := .

.PHONY: build run dev clean

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
# Requires .env file with GOOGLE_API_KEY
run:
	docker run -p 8000:8000 --env-file .env $(IMAGE_NAME)

# Run locally in development mode with reload
dev:
	adk web $(AGENTS_DIR) --reload_agents --port 8000

# Remove the Docker image
clean:
	docker rmi $(IMAGE_NAME)
