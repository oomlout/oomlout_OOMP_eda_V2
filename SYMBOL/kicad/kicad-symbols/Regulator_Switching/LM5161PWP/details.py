
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5161PWP"
    hexID = "SZKREGULATORSWITCHINGLM5161PWP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5161PWP', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-14-1EP_4.4x5mm_P0.65mm_EP3.4x5mm_Mask3x3.1mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5161.pdf', 'kicadSymbolki_keywords': 'step-down dc-dc buck regulator adjustable', 'kicadSymbolki_description': '1A Synchronous Buck/Fly-buck Converter, 4.5V-100V input, adjustable output voltage, HTSSOP-14', 'kicadSymbolki_fp_filters': 'HTSSOP*1EP*4.4x5*P0.65mm*'}])
    newPart['name'].append('LM5161PWP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

