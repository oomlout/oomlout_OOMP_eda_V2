
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TLP290-4"
    hexID = "SZKISOLATORTLP294"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP290-4', 'kicadSymbolFootprint': 'Package_SO:SOP-16_4.55x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=12855&prodName=TLP290-4', 'kicadSymbolki_keywords': 'NPN AC DC Quad Phototransistor Optocoupler', 'kicadSymbolki_description': 'Quad AC/DC Phototransistor Optocoupler, Vce 80V, CTR 50-600%, SOP16', 'kicadSymbolki_fp_filters': 'SOP*4.55x10.3mm*P1.27mm*'}])
    newPart['name'].append('TLP290-4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

