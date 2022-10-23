
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "NCP1077P065"
    hexID = "SZKREGULATORSWITCHINGNCP177P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCP1070P065', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP1077P065', 'kicadSymbolFootprint': 'Package_DIP:DIP-8-N7_W7.62mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NCP1070-D.PDF', 'kicadSymbolki_keywords': 'SMPS Converter', 'kicadSymbolki_description': 'High-Voltage Switcher for Low Power Offline SMPS, 700V Vds, 25W/15W, 230V/85-265V, 65kHz, 4.7Ohm Rds(on), 800mA Ipk, DIP-7', 'kicadSymbolki_fp_filters': 'DIP*N7*W7.62mm*'}])
    newPart['name'].append('NCP1077P065')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

