import pytest
from calcular_area import calcular_area

def test_area_valida():
    assert calcular_area(5, 7) == 17.5

def test_base_negativa():
    with pytest.raises(ValueError, match="base"):
        calcular_area(-3, 6)

def test_altura_negativa():
    with pytest.raises(ValueError, match="altura"):
        calcular_area(4, -2)

def test_base_cero():
    with pytest.raises(ValueError, match="base"):
        calcular_area(0, 5)
