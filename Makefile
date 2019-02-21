EXAMPLE = example

build:  ## Create example from cookiecutter template
	cookiecutter --overwrite-if-exists --no-input --config-file ./sample_config .

test:  ## Test generated example
	cd $(EXAMPLE) && \
		make docker-build docker-test && \
		make virtualenv-create virtualenv-test && \
		echo "TEST SUCCESSFUL"

clean:
	rm -rf $(EXAMPLE)
