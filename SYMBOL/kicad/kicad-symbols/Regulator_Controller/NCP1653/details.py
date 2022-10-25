
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "NCP1653"
    hexID = "SZKREGULATORCONTROLLERNCP1653"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP1653', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCP1653-D.PDF', 'kicadSymbolki_keywords': 'PFC SMPS Controller', 'kicadSymbolki_description': 'Compact, Fixed-Frequency, Continuous Conduction Mode PFC Controller, 100kHz, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Controller : NCP1653')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

