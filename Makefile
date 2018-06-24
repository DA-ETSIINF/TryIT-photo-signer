
NAME="tryitphotosigner_script"

all: prod

prod: _build _run

dev: _build _rundev


_build:
	@docker-compose build

_run:
	@docker-compose up -d

_rundev:
	@docker run -it --rm $(NAME) bash 

# to clean
# docker rm -v -f $(docker ps -a -q --filter="name=tryitphotosigner*" | sort)
# docker rmi $(docker images --filter reference="tryitphotosigner*" --quiet)