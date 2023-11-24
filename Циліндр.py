import math

def calcVolumeOfСylinder(diameter, height):
    return math.pi * diameter ** 2 / 4 * height


def compareVolumeOfCylinders(volume1, volume2):
    result = 'Об’єм {indexOfCylinder} циліндра більший'

    if volume1 > volume2:
        return result.format(indexOfCylinder = 'першого')
    elif volume1 == volume2:
        return 'Об’єми обох циліндрів рівні'
    else:
        return result.format(indexOfCylinder = 'другого')
    

diameter = float(input('Введіть діаметр першого циліндра: '))
height = float(input('Введіть висоту першого циліндра: '))

volumeOfСylinder1 = calcVolumeOfСylinder(diameter, height)
volumeOfСylinder2 = calcVolumeOfСylinder(height, diameter)

print(f'Об’єм перщого циліндра: {volumeOfСylinder1}')
print(f'Об’єм другого циліндра: {volumeOfСylinder2}')
print(compareVolumeOfCylinders(volumeOfСylinder1, volumeOfСylinder2))