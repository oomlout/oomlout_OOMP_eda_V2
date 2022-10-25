
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AP131-18"
    hexID = "SZKREGULATORLINEARAP13118"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AP131-15', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AP131-18', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.diodes.com/_files/datasheets/AP131.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo fixed positive', 'kicadSymbolki_description': '300mA low dropout linear regulator, shutdown pin, 1.8V fixed positive output, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : AP131-18')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

