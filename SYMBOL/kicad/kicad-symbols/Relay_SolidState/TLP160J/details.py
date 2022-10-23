
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay_SolidState"
    oIndex = "TLP160J"
    hexID = "SZKRELAYSOLIDSTATETLP16J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLP160G', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP160J', 'kicadSymbolFootprint': 'Package_SO:MFSOP6-4_4.4x3.6mm_P1.27mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=16919&prodName=TLP160J', 'kicadSymbolki_keywords': 'Opto-Triac Opto Triac Random', 'kicadSymbolki_description': 'Random Phase Opto-Triac, Vdrm 600V, Ift 7mA, SOP6', 'kicadSymbolki_fp_filters': 'MFSOP6*4.4x3.6mm*P1.27mm*'}])
    newPart['name'].append('TLP160J')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

