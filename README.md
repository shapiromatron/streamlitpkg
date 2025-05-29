# streamlitpkg

Demonstrate deploying a streamlit application nested within a Python package on [Posit Connect Cloud](https://connect.posit.cloud/).

This goes one step further than the excellent Posit [guide](https://docs.posit.co/connect-cloud/how-to/python/streamlit.html) that shows a simpler single module deployment. For our use case, we have a Python package, and one module within a package is the streamlit app.

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

As of May 2025, a little troubleshooting was required, see https://forum.posit.co/t/201304. Here are the two edits required:

1. Added a requirements.txt and manually keep synced w/ contents of `pyproject.toml`
2. Use absolute imports (`from work import foo`) instead of relative imports (`from .work import foo`) in the streamlit application, since the entrypoint for the app is the file itself and not the package.

Hopefully these nuances can be resolved in the future, documenting these findings in case they're helpful.

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
