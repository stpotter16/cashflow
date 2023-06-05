import nox

nox.options.sessions = "lint", "tests"


@nox.session(python=["3.10", "3.9", "3.8"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")


locations = "cashflow", "tests", "noxfile.py"


@nox.session(python=["3.10", "3.9", "3.8"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-black", "flake8-import-order")
    session.run("flake8", *args)


@nox.session(python="3.10")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
