
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "3SK263"
    hexID = "SZKTRANSISTORFET3SK263"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': '3SK263', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-143', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/EN4423-D.PDF', 'kicadSymbolki_keywords': 'N-Channel MOSFET Dual Gate', 'kicadSymbolki_description': '30mA Id, 15V Vds, N-Channel Dual Gate MOSFET, SOT-143/343', 'kicadSymbolki_fp_filters': 'SOT?143*'}])
    newPart['name'].append('Transistor_FET : 3SK263')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

