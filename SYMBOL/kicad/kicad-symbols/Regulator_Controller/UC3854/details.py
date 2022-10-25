
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "UC3854"
    hexID = "SZKREGULATORCONTROLLERUC3854"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'UC3854', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/uc3854.pdf', 'kicadSymbolki_keywords': 'PFC SMPS Controller', 'kicadSymbolki_description': 'High-Power Factor Preregulator, DIP-16/SOIC-16W', 'kicadSymbolki_fp_filters': 'SOIC*7.5x10.3mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Controller : UC3854')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

