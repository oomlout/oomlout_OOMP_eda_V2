
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF"
    oIndex = "MOC3051M"
    hexID = "SZKRFMOC351M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MOC3010M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MOC3051M', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MOC3052M-D.PDF', 'kicadSymbolki_keywords': 'Opto-Triac Opto Triac Random Phase', 'kicadSymbolki_description': 'Random Phase Opto-Triac, Vdrm 600V, Ift 15mA, DIP6', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SMDIP*W9.53mm* DIP*W10.16mm*'}])
    newPart['name'].append('RF : MOC3051M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

