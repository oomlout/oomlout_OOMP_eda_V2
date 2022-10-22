
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Conn_Coaxial_x2_Isolated"
    hexID = "SZKCNCONNCOAXIALX2ISOLATED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Conn_Coaxial_x2_Isolated', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ' ~', 'kicadSymbolki_keywords': 'BNC SMA SMB SMC LEMO coaxial connector CINCH RCA', 'kicadSymbolki_description': 'coaxial connector (BNC, SMA, SMB, SMC, Cinch/RCA, LEMO, ...)', 'kicadSymbolki_fp_filters': '*BNC* *SMA* *SMB* *SMC* *Cinch* *LEMO*'}])
    newPart['name'].append('Conn_Coaxial_x2_Isolated')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

