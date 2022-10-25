
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "DIN41612_01x32_A"
    hexID = "SZKCNDIN416121X32A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'DIN41612_01x32_A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'DIN41612 connector, single row (A), 01x32, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'DIN41612*1x*'}])
    newPart['name'].append('Connector : DIN41612_01x32_A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

