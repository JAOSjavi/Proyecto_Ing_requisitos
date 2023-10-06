class Calculadora:

    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def calcular(self, operacion):
        if operacion == "Suama":
            return self.operando1 + self.operando2
        elif operacion == "Restar":
            return self.operando1 - self.operando2
        elif operacion == "Multiplicar":
            return self.operando1 * self.operando2
        elif operacion == "Dividir":
            if self.operando2 == 0:
                raise ZeroDivisionError("No se puede dividir entre 0")
            return self.operando1 / self.operando2
        else:
            raise ValueError("Operación no valida")


def main():
    operando1 = int(input("Por favor digite el primer valor: "))
    operando2 = int(input("Por favor digite el segundo valor: "))
    calculadora = Calculadora(operando1, operando2)
    operaciones = input("Ingrese las operaciones que va a realizar (Sumar, Restar, Multiplicar, Dividir): ").lower()
    resultados = [calculadora.calcular(operacion) for operacion in operaciones.split()]
    print("El resultado de los numeros que digito es", resultados)


if __name__ == "__main__":
    main()