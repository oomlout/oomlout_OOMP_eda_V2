
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "ICL7663"
    hexID = "SZKREGULATORLINEARICL7663"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICL7663', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/ICL7663.pdf', 'kicadSymbolki_keywords': 'Linear Regulator 50mA 5V fixed', 'kicadSymbolki_description': '50mA 5V/Programmable Voltage Regulator, DIP-8/SO-8/TO-99', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm* TO?99*'}])
    newPart['name'].append('Regulator_Linear : ICL7663')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

