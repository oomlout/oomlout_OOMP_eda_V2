
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AZ1117H-ADJ"
    hexID = "SZKREGULATORLINEARAZ1117HADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM317_SOT-223', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AZ1117H-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/products_inactive_data/AZ1117.pdf', 'kicadSymbolki_keywords': 'Adjustable Voltage Regulator 1A Positive LDO', 'kicadSymbolki_description': '1A 20V Adjustable LDO Linear Regulator, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*TabPin2*'}])
    newPart['name'].append('Regulator_Linear : AZ1117H-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

