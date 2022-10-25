
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "DG9421DV"
    hexID = "SZKANALOGSWITCHDG9421DV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DG9421DV', 'kicadSymbolFootprint': 'Package_SO:TSOP-6_1.65x3.05mm_P0.95mm', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/70679/dg9421.pdf', 'kicadSymbolki_keywords': 'CMOS Analog Switch', 'kicadSymbolki_description': 'Single SPST Precision Low-Voltage, Low-Glitch CMOS Analog Switch, normally ON, 2Ohm Ron, TSOP-6', 'kicadSymbolki_fp_filters': 'TSOP*1.65x3.05mm*P0.95mm*'}])
    newPart['name'].append('Analog_Switch : DG9421DV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

