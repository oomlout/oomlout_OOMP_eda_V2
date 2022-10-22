
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "PG001M"
    hexID = "SZKDRIVERMOTORPG1M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PG001M', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Sanken/Datasheets/PG001M-Datasheet.ashx', 'kicadSymbolki_keywords': 'Support IC for SLA7042M/SLA7044M', 'kicadSymbolki_description': 'Parallel to serial data converter for SLA7042M/SLA7044M', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('PG001M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

