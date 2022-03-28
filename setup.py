import setuptools

# https://click.palletsprojects.com/en/8.0.x/setuptools/#introduction
setuptools.setup(
    name='cli_socket',
    version='0.1.0',
    py_modules=['cli_socket'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'cli_socket = scripts/cli_socket:cli',
        ],
    },
)