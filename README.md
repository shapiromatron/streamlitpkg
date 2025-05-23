# streamlitpkg

Demonstrate deploying a streamlit application nested within a Python package on [Posit Connect Cloud](https://connect.posit.cloud/).

This goes one step further than the excellent Posit [guide](https://docs.posit.co/connect-cloud/how-to/python/streamlit.html) that shows a simpler single module deployment. For our use case, we have a Python package, and one module within a package is the streamlit app.

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

Still troubleshooting deployment; see https://forum.posit.co/t/201304

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
