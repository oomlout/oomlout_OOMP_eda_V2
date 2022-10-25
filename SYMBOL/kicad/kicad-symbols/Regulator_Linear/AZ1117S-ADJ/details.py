
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AZ1117S-ADJ"
    hexID = "SZKREGULATORLINEARAZ1117SADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM317_TO-263', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AZ1117S-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-2', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/products_inactive_data/AZ1117.pdf', 'kicadSymbolki_keywords': 'Adjustable Voltage Regulator 1A Positive LDO', 'kicadSymbolki_description': '1A 20V Adjustable LDO Linear Regulator, TO-263', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Regulator_Linear : AZ1117S-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

