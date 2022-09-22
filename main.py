import pytest


def always_returns_true():
    print("hey")


def test_always_returns_true():
    assert always_returns_true()
