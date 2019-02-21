def pytest_collection_modifyitems(session, config, items):
    # Don't run tests if we want to lint only
    if config.getoption('--flake8') or config.getoption('--isort'):
        items[:] = [item for item in items
                    if item.get_marker('flake8')
                    or item.get_marker('isort')]
