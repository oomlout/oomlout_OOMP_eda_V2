
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "2SC4213"
    hexID = "SZKTRANSISTORBJT2SC4213"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC817W', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': '2SC4213', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-323_SC-70', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=19305&prodName=2SC4213', 'kicadSymbolki_keywords': 'NPN Transistor', 'kicadSymbolki_description': '0.3A Ic, 20V Vce, NPN Transistor, For Muting and Switching, SOT-323', 'kicadSymbolki_fp_filters': 'SOT?323*'}])
    newPart['name'].append('Transistor_BJT : 2SC4213')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

