
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "SC33063AD"
    hexID = "SZKREGULATORSWITCHINGSC3363AD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC33063AD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SC33063AD', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/MC34063A-D.PDF', 'kicadSymbolki_keywords': 'smps buck boost inverting', 'kicadSymbolki_description': '1.5A, step-up/down/inverting switching regulator, 3-40V Vin, 100kHz, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : SC33063AD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

