import nox

@nox.session(python=["3.10", "3.9", "3.8"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")

locations = "cashflow", "tests", "noxfile.py"

@nox.session(python=["3.10", "3.9", "3.8"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8")
    session.run("flake8", *args)
