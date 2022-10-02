import pytest

from adventofcode2021.utils.stack import Stack


def test_stack():
    st = Stack()

    # Check if empty
    assert st.empty

    # Popping empty should raise index error
    with pytest.raises(IndexError):
        st.pop()

    # Add some items
    st.push(1)
    st.push(2)
    st.push(3)

    # We should have some data now
    assert not st.empty

    # Let's look at the data
    assert repr(st) == repr([1, 2, 3])

    # Stack, to the Last In, First Out.
    assert st.pop() == 3
    assert st.pop() == 2
    assert st.pop() == 1

    # Should be empty again
    assert st.empty
    assert repr(st) == repr([])

    with pytest.raises(IndexError):
        st.pop()
