
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "OPOS6UL"
    hexID = "SZKMCUMOOPOS6UL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPOS6UL', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.opossom.com/_downloads/opos6ul/documentation/datasheet_opos6ul.pdf', 'kicadSymbolki_keywords': 'armadeus systems opos6ul sbc som compute module', 'kicadSymbolki_description': 'Armadeus Systems i.MX6UL based single board computer, SODIMM', 'kicadSymbolki_fp_filters': '*SODIMM*'}])
    newPart['name'].append('OPOS6UL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

