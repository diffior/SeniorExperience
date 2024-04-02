import re


def bad_input_exception(input, pattern, invalid_message):
    if pattern.match(input) is None:
        error_message = f"Error: {invalid_message}"
        print(error_message)  # Print the error message
        raise ValueError(error_message)  # Raise a ValueError with the error message
"""    try:
        if pattern.match(input) is None:
            print(invalid_message)  # bad __ input, create exception
    except TypeError:
        print(invalid_message)"""

def hostInput(input):
    if input is not None:
        host = re.compile('^[a-zA-Z0-9 ]+$|^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
        bad_input_exception(input, host, "Bad host input")

hostInput("169.0.0.4")


def stateInput(input):
    state = re.compile(r'\b(present|absent)\b', re.IGNORECASE)
    bad_input_exception(input, state, "Bad state input")


stateInput("present")


def nameSubjectInput(input):
    name = re.compile("^[a-zA-Z0-9 ,.?!@#$%^&*()<'>;:/_+=-]+$")
    bad_input_exception(input, name, "Bad name/subject input")


nameSubjectInput("Home Host Server")


def portInput(input):
    port = re.compile('^[0-9]{1,5}$')
    bad_input_exception(input, port, "Bad port input")

portInput("2556")

def emailInput(input):
    email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    bad_input_exception(input, email, "Bad email input")


emailInput("gradyrow@hotmail.com")


def bodyMsgInput(input):
    bodyMsg = re.compile('^"[a-zA-Z0-9 ,.?!@#$%^&*()<>;:/_+=-]+"$')
    bad_input_exception(input, bodyMsg, "Bad body/msg input")


bodyMsgInput('"This is and email notification"')

def commandInput(input):
    command = re.compile("^[a-zA-Z0-9 ,.?!@#$%^&*()<'>;:/_+=-]+$")
    bad_input_exception(input, command, "Bad command input")


commandInput("echo 'Hello from Ansible' > /tmp/output.txt")


def countInput(input):
    count = re.compile("^[0-9]+$")
    bad_input_exception(input, count, "Bad count input")


countInput("1")


def unitInput(input):
    unit = re.compile(r'\b(seconds|minutes|hours|days)\b', re.IGNORECASE)
    bad_input_exception(input, unit, "Bad unit input")


unitInput("minutes")


def timespecInput(input):
    timespec = re.compile(r'^(now \+ \d+ (seconds?|minutes?|hours?|days?)|\d{4}|\d{12}|\d{4}-\d{2}-\d{2}T\d{2}:\d{2})$', re.IGNORECASE)
    bad_input_exception(input, timespec, "Bad timespec input")


timespecInput("now + 12 hours")
timespecInput("2300")
timespecInput("201807012300")
timespecInput("2018-07-01T23:00")

def repoInput(input):
    repo = re.compile(r'^https://github\.com/[^/]+/[^/]+\.git$')
    bad_input_exception(input, repo, "Bad repo input")


repoInput('https://github.com/example/repo.git')


def destInput(input):
    dest = re.compile(r'^/[^/]+(/[^/]*)*$')
    bad_input_exception(input, dest, "Bad dest input")


destInput('/path/to/the/destination')

