import pathlib
import time

from django_static_url_helper import url_helper


def test_now_helper():
    url1 = url_helper.get_static_url_now("/static/", False)
    assert url1.startswith("/static/")
    assert len(url1) > len("/static/")
    assert url1.endswith("/")

    url2 = url_helper.get_static_url_now("/static/", True, "abc")
    time.sleep(1.1)
    url3 = url_helper.get_static_url_now("/static/", True, "abc")
    assert url2 != url3


def test_file_helper():
    url1 = url_helper.get_static_url_file(
        "/static/", __file__, True, "abc")
    assert url1.startswith("/static/")
    assert len(url1) > len("/static/")
    assert url1.endswith("/")

    time.sleep(0.5)
    path = pathlib.Path(__file__)
    path.touch()
    url2 = url_helper.get_static_url_file(
        "/static/", __file__, True, "abc")
    assert url1 != url2
