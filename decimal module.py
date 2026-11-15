import decimal
import fractions

a = decimal.Decimal("0.1")#No floats only strings
b = decimal.Decimal("0.2")
print(a + b)
#=
print(decimal.Decimal(0.1) + decimal.Decimal(0.2))#any operator works

decimal.getcontext().prec = 5
x = decimal.Decimal("1") / decimal.Decimal("3")
print(x)
decimal.getcontext().prec = 50
print(decimal.Decimal("20") / decimal.Decimal("3")) 
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

y = decimal.Decimal("2.345")
print(y.quantize(decimal.Decimal("0.01")))  # 2.35

print(decimal.Decimal("1") / decimal.Decimal("3"))   # decimal approximation
print(fractions.Fraction(1, 3))                      # exact fraction              