# coding=Cp1252
# **Exercício 3: Conversor de Temperatura** - Converta uma temperatura dada em Celsius para Fahrenheit. 
# A fórmula é `F = C * 9/5 + 32`. ### Nível Médio 

class Fahrenheit(float):
  def to_celcius(self) -> float:
    return (self - 32) * 5/9
  
class Celcius(float):
  def to_fahrenheit(self) -> float:
    return (self * 9/5) + 32

print(Fahrenheit(100).to_celcius()) # 100 F = 37.77777777777778 C

print(Celcius(50).to_fahrenheit()) # 50 C = 122.22222222222223 F

print(Fahrenheit(Fahrenheit(50) + Celcius(50).to_fahrenheit()).to_celcius()) 
# 50 C + 50 F = 50 F + 122.22222222222223 F = 77.77777777777779 C