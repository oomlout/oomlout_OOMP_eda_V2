
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "SiA449DJ"
    hexID = "SZKTRANSISTORFETSIA449DJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SiA453EDJ', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'SiA449DJ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Vishay_PowerPAK_SC70-6L_Single', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/62644/sia449dj.pdf', 'kicadSymbolki_keywords': 'P-Channel MOSFET', 'kicadSymbolki_description': '-12A Id, -30V Vds, P-Channel MOSFET, PowerPAK SC70-6', 'kicadSymbolki_fp_filters': 'Vishay*PowerPAK*SC70*Single*'}])
    newPart['name'].append('Transistor_FET : SiA449DJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

