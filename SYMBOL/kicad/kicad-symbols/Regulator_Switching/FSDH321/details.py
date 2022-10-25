
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "FSDH321"
    hexID = "SZKREGULATORSWITCHINGFSDH321"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FSDH321', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FSDH321JP-D.pdf', 'kicadSymbolki_keywords': 'SMPS Controller with MOSFET 17W AC-DC', 'kicadSymbolki_description': '17W SMPS Controller, 100kHz, AC-DC, PDIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Switching : FSDH321')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

