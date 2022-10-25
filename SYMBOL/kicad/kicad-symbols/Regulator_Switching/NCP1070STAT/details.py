
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "NCP1070STAT"
    hexID = "SZKREGULATORSWITCHINGNCP17STAT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP1070STAT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NCP1070-D.PDF', 'kicadSymbolki_keywords': 'SMPS Converter', 'kicadSymbolki_description': 'High-Voltage Switcher for Low Power Offline SMPS, 700V Vds, 14W/7.75W, 230V/85-265V, 65kHz, 22Ohm Rds(on), 250mA Ipk, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Regulator_Switching : NCP1070STAT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

