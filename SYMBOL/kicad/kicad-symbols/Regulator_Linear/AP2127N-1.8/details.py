
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AP2127N-1.8"
    hexID = "SZKREGULATORLINEARAP2127N18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'APE8865N-12-HF-3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AP2127N-1.8', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AP2127.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo fixed positive', 'kicadSymbolki_description': '300mA low dropout linear regulator, shutdown pin, 2.5V-6V input voltage, 1.8V fixed positive output, SOT-23 package', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : AP2127N-1.8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

