
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RJ45_Abracon_ARJP11A-MASA-B-A-EMU2"
    hexID = "SZKCNRJ45ABRACONARJP11AMASABAEMU2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RJ45_Abracon_ARJP11A-MASA-B-A-EMU2', 'kicadSymbolFootprint': 'Connector_RJ:RJ45_Abracon_ARJP11A-MA_Horizontal', 'kicadSymbolDatasheet': 'https://abracon.com/Magnetics/lan/ARJP11A.PDF', 'kicadSymbolki_keywords': 'single port ethernet transformer poe center-tap', 'kicadSymbolki_description': 'RJ45 PoE 10/100 Base-TX Jack with Magnetic Module', 'kicadSymbolki_fp_filters': 'RJ45*Abracon*ARJP11A?MA*'}])
    newPart['name'].append('Connector : RJ45_Abracon_ARJP11A-MASA-B-A-EMU2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

