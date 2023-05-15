import pytest
import requests


class GoGetter:
    """
    The thing I am testing, this is usually imported into the test file, but
    defined here for simplicity.
    """

    def get(self):
        """
        Get the content of `https://waylonwalker.com` and return it as a string
        if successfull, or False if it's not found.
        """
        r = requests.get("https://waylonwalker.com")
        if r.status_code == 200:
            return r.content
        if r.status_code == 404:
            return False


class DummyRequester:
    def __init__(self, content, status_code):
        """
        mock out content and status_code
        """

        self.content = content
        self.status_code = status_code

    def __call__(self, url):
        """
        The way I set this up GoGetter is going to call an instance of this
        class, so the easiest way to make it work was to implement __call__.
        """
        self.url = url
        return self


def test_success_get(mocker):
    """
    Show that the GoGetter can handle successful calls.
    """
    go_getter = GoGetter()

    # Use the mocker fixture to change how requests.get works while inside of test_success_get
    mocker.patch.object(requests, "get", DummyRequester("waylonwalker", 200))
    assert "waylon" in go_getter.get()


def test_failed_get(mocker):
    """
    Show that the GoGetter can handle failed calls.
    """
    go_getter = GoGetter()

    # Use the mocker fixture to change how requests.get works while inside of test_failed_get
    mocker.patch.object(requests, "get", DummyRequester("waylonwalker", 404))
    assert go_getter.get() is False


if __name__ == '__main__':
    pytest.main(['-vs'])
