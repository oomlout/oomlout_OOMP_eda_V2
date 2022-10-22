
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "ISD2590E"
    hexID = "SZKAUDIOISD259E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ISD2560E', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISD2590E', 'kicadSymbolFootprint': 'Package_SO:TSOP-I-28_11.8x8mm_P0.55mm', 'kicadSymbolDatasheet': 'https://datasheetspdf.com/pdf-file/700027/Winbond/ISD2560/1', 'kicadSymbolki_keywords': 'isd2590', 'kicadSymbolki_description': 'Single-Chip Voice Record/Playback Device 90-Second Duration, TSOP-I-28', 'kicadSymbolki_fp_filters': 'TSOP*11.8x8mm*P0.55mm*'}])
    newPart['name'].append('ISD2590E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

