
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "HCPL-314J"
    hexID = "SZKDRIVERFETHCPL314J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HCPL-314J', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W-12_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-0169EN', 'kicadSymbolki_keywords': 'MOSFET Driver IGBT Driver Optocoupler', 'kicadSymbolki_description': 'Gate Drive Optocoupler, Output Current 0.4/0.4A, SOIC-16(12)', 'kicadSymbolki_fp_filters': 'SOIC*16*12*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('HCPL-314J')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

