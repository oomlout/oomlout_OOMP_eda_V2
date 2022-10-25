
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Switch"
    oIndex = "KSWHA-1-20"
    hexID = "SZKRFSWITCHKSWHA12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KSWHA-1-20', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/KSWHA-1-20+.pdf', 'kicadSymbolki_keywords': 'RF SPST switch', 'kicadSymbolki_description': 'SPST DC-2.0GHz absorbative switch, 50 Ohm, XX112', 'kicadSymbolki_fp_filters': 'Mini?Circuits*XX112* SOP*1EP*4.57x4.57mm*P1.27mm*'}])
    newPart['name'].append('RF_Switch : KSWHA-1-20')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

