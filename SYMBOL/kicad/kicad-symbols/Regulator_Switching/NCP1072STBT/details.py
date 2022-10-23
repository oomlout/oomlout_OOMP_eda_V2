
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "NCP1072STBT"
    hexID = "SZKREGULATORSWITCHINGNCP172STBT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCP1070STAT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP1072STBT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NCP1070-D.PDF', 'kicadSymbolki_keywords': 'SMPS Converter', 'kicadSymbolki_description': 'High-Voltage Switcher for Low Power Offline SMPS, 700V Vds, 19W/10W, 230V/85-265V, 100kHz, 11Ohm Rds(on), 250mA Ipk, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('NCP1072STBT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

