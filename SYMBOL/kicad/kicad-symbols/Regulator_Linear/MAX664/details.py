
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MAX664"
    hexID = "SZKREGULATORLINEARMAX664"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX664', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://pdfserv.maximintegrated.com/en/ds/MAX663-MAX666.pdf', 'kicadSymbolki_keywords': 'Linear LDO Regulator 50mA -5V fixed negative', 'kicadSymbolki_description': '50mA Dual Mode -5V/Programmable Micropower Negative Voltage Regulator, DIP-8/SO-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Linear : MAX664')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

