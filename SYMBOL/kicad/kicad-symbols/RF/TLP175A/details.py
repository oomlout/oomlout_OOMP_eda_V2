
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF"
    oIndex = "TLP175A"
    hexID = "SZKRFTLP175A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP175A', 'kicadSymbolFootprint': 'Package_SO:MFSOP6-4_4.4x3.6mm_P1.27mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=13665&prodName=TLP175A', 'kicadSymbolki_keywords': 'MOSFET Output Photorelay 1-Form-A', 'kicadSymbolki_description': 'MOSFET Photorelay 1-Form-A, Voff 60V, Ion 100mA, SOP6', 'kicadSymbolki_fp_filters': 'MFSOP6*4.4x3.6mm*P1.27mm*'}])
    newPart['name'].append('RF : TLP175A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

