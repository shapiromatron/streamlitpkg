# streamlitpkg

Demonstrate deploying a streamlit application nested within a python package on [Posit Connect Cloud](https://connect.posit.cloud/).

This goes one step further than the excellent Posit [guide](https://docs.posit.co/connect-cloud/how-to/python/streamlit.html) that shows a simpler single module deployment. For our use case, we have a python package, and one module within a package is the streamlit app.

We're targeting the Posit Connect Cloud instead of the Streamlit [cloud](https://streamlit.io/cloud) because using the streamlit cloud requires admin level access to streamlit in a GitHub repository, which we don't want to do.

## Quickstart

Install [uv](https://docs.astral.sh/uv/) and make it available and on your path. Then:

```bash
# update and install
uv sync

# run using streamlit directly
uv run streamlit run src/streamlitpkg/app.py

# or run using a custom package entrypoint
uv run streamlitpkg run-app
```

## Deploying to Posit Connect Cloud

As of May 22, 2025, I'm unable to deploy:

```
2025-05-22T20:35:58-04:00 Your publish request with ID 725f3707-456a-4553-b4d5-0bbdf429b2bc is now being processed.
2025-05-22T20:35:58-04:00 Loading your source code...
2025-05-22T20:35:58-04:00 Initialized empty Git repository in /cloud/project/.git/
2025-05-22T20:35:59-04:00 From https://github.com/shapiromatron/streamlitpkg
2025-05-22T20:35:59-04:00  * branch            d5f82ab1b8ea75b29967865dd474a95f41f2b3fc -> FETCH_HEAD
2025-05-22T20:35:59-04:00 HEAD is now at d5f82ab rollback to version 3.12
2025-05-22T20:35:59-04:00 Error determining requirements: / does not appear to be a Python project, as neither `pyproject.toml` nor `setup.py` are present in the directory
2025-05-22T20:35:59-04:00 Failed to publish content: This content's dependencies could not be resolved. Check your requirements.txt. error_id=e628b7c0-7788-4147-97be-00056e71b171
```

The `requirements.txt` includes just a single line `.`, which should resolve to `pip install .`.   This should be equivalent to installing this package in the current environment.

## Developer setup

Make sure you have uv available on your path. Then:

```bash
# clone project
git clone git@github.com:shapiromatron/streamlitpkg.git
cd streamlitpkg

# create virtual environment and activate
uv sync --all-extras

# run assorted commands
uv run poe --help
uv run poe test    # run tests
uv run poe lint    # identify formatting errors
uv run poe format  # fix formatting errors when possible
uv run poe build   # build a python wheel
```

Github actions are set up to execute whenever code is pushed to check code formatting and successful tests. In addition, when code is pushed to the `main` branch, a wheel artifact is created and stored on github.
