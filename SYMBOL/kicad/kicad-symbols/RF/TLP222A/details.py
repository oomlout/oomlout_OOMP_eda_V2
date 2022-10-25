
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF"
    oIndex = "TLP222A"
    hexID = "SZKRFTLP222A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP222A', 'kicadSymbolFootprint': 'Package_DIP:DIP-4_W7.62mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=17036&prodName=TLP222A', 'kicadSymbolki_keywords': 'MOSFET Output Photorelay 1-Form-A', 'kicadSymbolki_description': 'MOSFET Photorelay 1-Form-A, Voff 60V, Ion 0,5A, DIP4', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('RF : TLP222A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

