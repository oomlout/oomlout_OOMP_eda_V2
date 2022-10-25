
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector_Generic_Shielded"
    oIndex = "Conn_01x23_Shielded"
    hexID = "SZKCNGENERICSHEDCONN1X23SHED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Conn_01x23_Shielded', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'Generic shielded connector, single row, 01x23, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_1x??-1SH*'}])
    newPart['name'].append('Connector_Generic_Shielded : Conn_01x23_Shielded')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

