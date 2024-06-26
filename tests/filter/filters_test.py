from __future__ import annotations

from taps.filter import NullFilter
from taps.filter import ObjectSizeFilter
from taps.filter import ObjectTypeFilter
from taps.filter import PickleSizeFilter


def test_null_filter() -> None:
    filter_ = NullFilter()
    assert filter_(object())


def test_object_size_filter() -> None:
    filter_ = ObjectSizeFilter(min_bytes=32, max_bytes=100)

    assert not filter_(object())
    assert filter_('object')
    assert not filter_('x' * 100)


def test_object_type_filter() -> None:
    filter_ = ObjectTypeFilter(str, tuple)

    assert filter_('object')
    assert filter_(())
    assert not filter_([])


def test_pickle_size_filter() -> None:
    filter_ = PickleSizeFilter(min_bytes=64, max_bytes=128)

    assert not filter_(object())
    assert filter_(b'x' * 80)
    assert not filter_(b'x' * 256)
