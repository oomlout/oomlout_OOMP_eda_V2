
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Switch"
    oIndex = "MSW-2-20"
    hexID = "SZKRFSWITCHMSW22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSW-2-20', 'kicadSymbolFootprint': 'Package_SO:SOP-8_3.76x4.96mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/MSW-2-20+.pdf', 'kicadSymbolki_keywords': 'RF SPDT switch', 'kicadSymbolki_description': 'SPDT DC-2.0GHz reflective switch, 50 Ohm, SOP-8', 'kicadSymbolki_fp_filters': 'SOP*3.76x4.96mm*P1.27mm*'}])
    newPart['name'].append('MSW-2-20')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

