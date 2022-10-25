
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector_Generic_MountingPin"
    oIndex = "Conn_01x31_MountingPin"
    hexID = "SZKCNGENERICMOUNTINGPINCONN1X31MOUNTINGPIN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Conn_01x31_MountingPin', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'Generic connectable mounting pin connector, single row, 01x31, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_1x??-1MP*'}])
    newPart['name'].append('Connector_Generic_MountingPin : Conn_01x31_MountingPin')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

