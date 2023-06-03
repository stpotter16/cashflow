import nox

@nox.session(python=["3.10", "3.9", "3.8"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")
