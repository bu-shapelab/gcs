#!/usr/bin/env bash

# Check for the correct number of arguments
if [ $# -lt 1 ] || [ $# -gt 2 ]; then
    echo "Usage: $0 <pypi|testpypi> [verbose]"
    exit 1
fi

# Valid deployment options
valid_deploy_options=("pypi" "testpypi")

# Check if the first argument is a valid deployment option
if [[ ! " ${valid_deploy_options[@]} " =~ " $1 " ]]; then
    echo "Error: Invalid deployment option. Allowed options: ${valid_deploy_options[*]}"
    echo "Usage: $0 <pypi|testpypi> [verbose]"
    exit 1
fi

# Remove existing dist directory
rm -rf dist

# Build distribution files
python -m build

# Check distribution files using twine
twine check dist/*

# Check for the command-line arguments
if [ "$1" = "pypi" ]; then
    # Deploy to PyPI
    if [ "$2" = "verbose" ]; then
        twine upload --verbose dist/*
    else
        twine upload dist/*
    fi
elif [ "$1" = "testpypi" ]; then
    # Deploy to PyPI Test
    if [ "$2" = "verbose" ]; then
        twine upload --verbose --repository testpypi dist/*
    else
        twine upload --repository testpypi dist/*
    fi
fi
