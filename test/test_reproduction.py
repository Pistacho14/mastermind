import pytest
from src.reproduction import reproduction

@pytest.mark.parametrize(
    'father, mother, offspring',
    [
        (
         ['Red', 'Red', 'Yellow', 'Yellow'],
         ['Yellow', 'Yellow', 'Red', 'Red'],
         [['Red', 'Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Yellow']]
        ),
        (
         ['Cyan', 'Purple', 'Orange', 'Yellow'],
         ['Yellow', 'Green', 'Red', 'Orange'],
         [['Cyan', 'Purple', 'Red', 'Orange'], ['Yellow', 'Green', 'Orange', 'Yellow']]
        ),
    ],
)

def test_reproduction(father, mother, offspring):
    assert reproduction(father, mother) == offspring
