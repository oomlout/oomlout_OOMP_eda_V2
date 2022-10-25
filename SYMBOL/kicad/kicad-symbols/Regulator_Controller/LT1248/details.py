
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "LT1248"
    hexID = "SZKREGULATORCONTROLLERLT1248"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1248', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1248fd.pdf', 'kicadSymbolki_keywords': 'pfc controller', 'kicadSymbolki_description': 'Power Factor Controller, DIP-16/SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*16*3.9x9.9mm*P1.27mm* DIP*16*W7.62mm*'}])
    newPart['name'].append('Regulator_Controller : LT1248')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

