
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "SiA453EDJ"
    hexID = "SZKTRANSISTORFETSIA453EDJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'SiA453EDJ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Vishay_PowerPAK_SC70-6L_Single', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/62864/sia453edj.pdf', 'kicadSymbolki_keywords': 'P-Channel MOSFET', 'kicadSymbolki_description': '-10A Id, -30V Vds, P-Channel MOSFET', 'kicadSymbolki_fp_filters': 'Vishay*PowerPAK*SC70*Single*'}])
    newPart['name'].append('Transistor_FET : SiA453EDJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

