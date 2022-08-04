#--Create a TemperatureConverter class, where you need to convert between Kelvin , celsius and Fahrenheit.--#

#--Creating TemperatureConverter class--#
class TemperatureConverter:

    def __init__(self):
        pass

    @staticmethod
    def celciusConversion(c):
        print('')
        print('Conversion of Celcius:')
        print(f'The temperature you entered is {c}°C:')
        c_to_f=(c*1.8)+32
        c_to_k=c+273.15
        print(f'Fahrenheit equivalent: {c_to_f}°F and Kelvin equivalent: {c_to_k}K')
        return (c_to_f,c_to_k)

    @staticmethod
    def fahrenheitConversion(f):
        print('')
        print('Conversion of Fahrenheit:')
        print(f'The temperature you entered is {f}°F:')
        f_to_c=(f-32)*0.5556
        f_to_k=(f-32)*0.5556 + 273.15
        print(f'Celcius equivalent: {f_to_c}°C and Kelvin equivalent: {f_to_k}K')
        return (f_to_c,f_to_k)

    @staticmethod
    def kelvinConversion(k):
        print('')
        print('Conversion of Kelvin:')
        print(f'The temperature you entered is {k}K:')
        k_to_c=k-273.15
        k_to_f=(k-273.15)*1.8 +32
        print(f'Celcius equivalent: {k_to_c}°C and Kelvin equivalent: {k_to_f}°F')
        return (k_to_c,k_to_f)


temp1=TemperatureConverter.celciusConversion(-7)
print(temp1)
temp2=TemperatureConverter.fahrenheitConversion(32)
print(temp2)
temp3=TemperatureConverter.kelvinConversion(-457)
print(temp3)