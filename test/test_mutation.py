import pytest
from src.mutation import mutation

@pytest.mark.parametrize(
    '''
    individuo, 
    probabilidad_de_mutar, 
    colores
    ''',
    [
        (
         ['Red', 'Red', 'Yellow', 'Yellow'],
         1,
         ['Red','Cyan','Yellow', 'Purple', 'Green', 'Orange'],
        ),
        (
         ['Cyan', 'Purple', 'Orange', 'Yellow'],
         1,
         ['Red','Cyan','Yellow', 'Purple', 'Green', 'Orange']

        ),
    ],
)

def test_mutation(individuo, probabilidad_de_mutar, colores):
    assert mutation(individuo, probabilidad_de_mutar, colores) != individuo
