
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "ZXBM5210-SP"
    hexID = "SZKDRIVERMOTORZXBM521SP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ZXBM5210-SP', 'kicadSymbolFootprint': 'Package_SO:Diodes_SO-8EP', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/ZXBM5210.pdf', 'kicadSymbolki_keywords': 'H-bridge, motor driver, PWM, single coil', 'kicadSymbolki_description': 'Reversible DC motor drive with speed control, 3-18V, 0.85A, SOIC-8EP', 'kicadSymbolki_fp_filters': 'Diodes*SO*EP*'}])
    newPart['name'].append('Driver_Motor : ZXBM5210-SP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

