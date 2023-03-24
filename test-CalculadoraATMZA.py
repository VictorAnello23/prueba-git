from src.CalculadoraATMZA import metros_cuadrados, metros_lineales, num_placas, precio_total

def test_metros_lineales():
    assert metros_lineales == 30

def test_metros_cuadrados():
    assert metros_cuadrados == 11.36

def test_num_placas():
    assert num_placas == 75

def test_precio_total():
    assert precio_total == 47250
