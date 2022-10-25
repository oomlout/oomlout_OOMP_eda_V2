
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector_Generic_MountingPin"
    oIndex = "Conn_02x17_Row_Letter_First_MountingPin"
    hexID = "SZKCNGENERICMOUNTINGPINCONN2X17ROWLETTERFIRSTMOUNTINGPIN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Conn_02x17_Row_Letter_First_MountingPin', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'Generic connectable mounting pin connector, double row, 02x17, row letter first pin numbering scheme (pin number consists of a letter for the row and a number for the pin index in this row. a1, ..., aN; b1, ..., bN), script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_2x??-1MP*'}])
    newPart['name'].append('Connector_Generic_MountingPin : Conn_02x17_Row_Letter_First_MountingPin')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

