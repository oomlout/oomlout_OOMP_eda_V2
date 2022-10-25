
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "SiP32431DR3"
    hexID = "SZKPOWERMANAGEMENTSIP32431DR3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SiP32431DR3', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.vishay.com.hk/docs/66597/sip32431.pdf', 'kicadSymbolki_keywords': 'Load switch', 'kicadSymbolki_description': '10 pA, Ultra Low Leakage and Quiescent Current, Load Switch with Reverse Blocking, High Enable, SC-70-6', 'kicadSymbolki_fp_filters': '*SC?70*'}])
    newPart['name'].append('Power_Management : SiP32431DR3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

