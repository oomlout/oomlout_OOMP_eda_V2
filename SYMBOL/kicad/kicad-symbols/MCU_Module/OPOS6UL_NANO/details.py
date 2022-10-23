
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "OPOS6UL_NANO"
    hexID = "SZKMCUMOOPOS6ULNANO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPOS6UL_NANO', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.opossom.com/_downloads/opos6ul_nano/datasheet_opos6ul_nano.pdf', 'kicadSymbolki_keywords': 'opos6ul compute module', 'kicadSymbolki_description': 'NXP i.MX6ULL/i.MX6UL, 256 or 512 MB RAM, industrial SoM computer, M.2M (NGFF)', 'kicadSymbolki_fp_filters': '*M.2*'}])
    newPart['name'].append('OPOS6UL_NANO')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

