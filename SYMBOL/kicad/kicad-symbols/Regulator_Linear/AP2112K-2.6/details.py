
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AP2112K-2.6"
    hexID = "SZKREGULATORLINEARAP2112K26"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AP2204K-1.5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AP2112K-2.6', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AP2112.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo fixed positive', 'kicadSymbolki_description': '600mA low dropout linear regulator, with enable pin, 3.1V-6V input voltage range, 2.6V fixed positive output, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23?5*'}])
    newPart['name'].append('Regulator_Linear : AP2112K-2.6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

