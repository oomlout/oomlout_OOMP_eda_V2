
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector_Generic"
    oIndex = "Conn_2Rows-21Pins"
    hexID = "SZKCNGENERICCONN2ROWS21PINS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Conn_2Rows-21Pins', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'Generic connector, double row, 21 pins, odd/even pin numbering scheme (row 1 odd numbers, row 2 even numbers), script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*2Rows*Pins__* *FCC*2Rows*Pins__*'}])
    newPart['name'].append('Conn_2Rows-21Pins')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

