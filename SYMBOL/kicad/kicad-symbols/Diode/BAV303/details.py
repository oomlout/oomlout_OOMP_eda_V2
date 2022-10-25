
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAV303"
    hexID = "SZKDIODEBAV33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCL4148', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAV303', 'kicadSymbolFootprint': 'Diode_SMD:D_MicroMELF', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/85545/bav300.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '200V 0.25A Switching Diode, High Voltage, MicroMELF', 'kicadSymbolki_fp_filters': 'D*MicroMELF*'}])
    newPart['name'].append('Diode : BAV303')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

