
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Switch"
    oIndex = "MSWA-2-20"
    hexID = "SZKRFSWITCHMSWA22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSWA-2-20', 'kicadSymbolFootprint': 'Package_SO:SOP-8_3.76x4.96mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/MSWA-2-20+.pdf', 'kicadSymbolki_keywords': 'RF SPDT switch', 'kicadSymbolki_description': 'SPDT DC-2.0GHz absorbative switch, 50 Ohm, SOP-8', 'kicadSymbolki_fp_filters': 'SOP*3.76x4.96mm*P1.27mm*'}])
    newPart['name'].append('RF_Switch : MSWA-2-20')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

