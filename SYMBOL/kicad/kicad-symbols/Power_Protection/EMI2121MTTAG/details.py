
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "EMI2121MTTAG"
    hexID = "SZKPOWERPROTECTIONEMI2121MTTAG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EMI2121MTTAG', 'kicadSymbolFootprint': 'Package_DFN_QFN:WDFN-8-1EP_2x2.2mm_P0.5mm_EP0.80x0.54', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/EMI2121MT-D.PDF', 'kicadSymbolki_keywords': 'Common Mode ESD', 'kicadSymbolki_description': 'Single Pair Common Mode Filter with ESD Protection, WDFN-8', 'kicadSymbolki_fp_filters': 'WDFN*1EP*2x2.2mm*P0.5mm*'}])
    newPart['name'].append('Power_Protection : EMI2121MTTAG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

