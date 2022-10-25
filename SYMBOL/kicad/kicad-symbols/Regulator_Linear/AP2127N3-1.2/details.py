
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AP2127N3-1.2"
    hexID = "SZKREGULATORLINEARAP2127N312"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AP2127N3-1.2', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AP2127.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo fixed positive', 'kicadSymbolki_description': '300mA low dropout linear regulator, shutdown pin, 2.5V-6V input voltage, 1.2V fixed positive output, SOT-23-3 package', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Regulator_Linear : AP2127N3-1.2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

