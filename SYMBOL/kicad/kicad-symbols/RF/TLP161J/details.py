
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF"
    oIndex = "TLP161J"
    hexID = "SZKRFTLP161J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLP161G', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP161J', 'kicadSymbolFootprint': 'Package_SO:MFSOP6-4_4.4x3.6mm_P1.27mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=4207&prodName=TLP161J', 'kicadSymbolki_keywords': 'Opto-Triac Opto Triac Zero Cross', 'kicadSymbolki_description': 'Zero Cross Opto-Triac, Vdrm 600V, Ift 7mA, SOP6', 'kicadSymbolki_fp_filters': 'MFSOP6*4.4x3.6mm*P1.27mm*'}])
    newPart['name'].append('RF : TLP161J')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

