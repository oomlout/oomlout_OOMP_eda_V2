
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "SZNUP2105L"
    hexID = "SZKPOWERPROTECTIONSZNUP215L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NUP2105L', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SZNUP2105L', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/NUP2105L-D.PDF', 'kicadSymbolki_keywords': 'can esd protection suppression transient automotive', 'kicadSymbolki_description': 'Dual Line CAN Bus Protector, 24Vrwm, Automotive Grade', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Power_Protection : SZNUP2105L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

