
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Switch"
    oIndex = "MSW2-50"
    hexID = "SZKRFSWITCHMSW25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSW2-50', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-12-1EP_3x3mm_P0.51mm_EP1.45x1.45mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/MSW2-50+.pdf', 'kicadSymbolki_keywords': 'RF SPDT switch', 'kicadSymbolki_description': 'SPDT DC-5.0GHz reflective switch, 50 Ohm, QFN-12', 'kicadSymbolki_fp_filters': 'QFN*1EP*3x3mm*P0.51mm*'}])
    newPart['name'].append('RF_Switch : MSW2-50')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

