
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "NCP1072P100"
    hexID = "SZKREGULATORSWITCHINGNCP172P1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCP1070P065', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP1072P100', 'kicadSymbolFootprint': 'Package_DIP:DIP-8-N7_W7.62mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NCP1070-D.PDF', 'kicadSymbolki_keywords': 'SMPS Converter', 'kicadSymbolki_description': 'High-Voltage Switcher for Low Power Offline SMPS, 700V Vds, 19W/10W, 230V/85-265V, 100kHz, 11Ohm Rds(on), 250mA Ipk, DIP-7', 'kicadSymbolki_fp_filters': 'DIP*N7*W7.62mm*'}])
    newPart['name'].append('NCP1072P100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

