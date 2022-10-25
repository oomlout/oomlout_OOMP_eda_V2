
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM22676MR-5"
    hexID = "SZKREGULATORSWITCHINGLM22676MR5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM22676MR-ADJ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM22676MR-5', 'kicadSymbolFootprint': 'Package_SO:TI_SO-PowerPAD-8', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm22676.pdf', 'kicadSymbolki_keywords': 'DC/DC Buck Converter 3A', 'kicadSymbolki_description': '3A Step-Down Switching Voltage Regulater, 4.5-42V Input, 5V Output, 500kHz Switching Frequency, SOIC-8', 'kicadSymbolki_fp_filters': 'TI*SO*PowerPAD*'}])
    newPart['name'].append('Regulator_Switching : LM22676MR-5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

