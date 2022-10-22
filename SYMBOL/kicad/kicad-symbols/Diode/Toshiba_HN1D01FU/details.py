
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "Toshiba_HN1D01FU"
    hexID = "SZKDIODETOSHIBAHN1D1FU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Rohm_UMP11N', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'Toshiba_HN1D01FU', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.toshiba.com/taec/components2/Datasheet_Sync/200901/DST_HN1D01FU-TDE_EN_1882.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Ultra High Speed Switching Diode Array 2 pair Com A', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Toshiba_HN1D01FU')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

