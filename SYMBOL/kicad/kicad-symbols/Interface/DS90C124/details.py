
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "DS90C124"
    hexID = "SZKINTERFACEDS9C124"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS90C124', 'kicadSymbolFootprint': 'Package_QFP:TQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ds90c241.pdf', 'kicadSymbolki_keywords': 'DC-Balanced 24-Bit FPD-Link II Deserializer', 'kicadSymbolki_description': 'DC-Balanced 24-Bit FPD-Link II Deserializer, TQFP-48', 'kicadSymbolki_fp_filters': 'TQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('Interface : DS90C124')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

