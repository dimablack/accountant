# Transaction service
    docker build . -f docker/transactions_app/Dockerfile
    docker-compose build
    docker-compose run --rm transactions_app_service sh -c "django-admin startproject app ."
