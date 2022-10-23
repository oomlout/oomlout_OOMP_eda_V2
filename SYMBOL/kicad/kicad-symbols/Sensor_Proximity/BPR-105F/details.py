
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "BPR-105F"
    hexID = "SZKSENPROXIMITYBPR15F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ITR8307-F43', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BPR-105F', 'kicadSymbolFootprint': 'OptoDevice:Everlight_ITR8307F43', 'kicadSymbolDatasheet': 'http://www.ystone.com.tw/en/data/goods/IRPT/Photo%20Interrupters-Reflective%20Type.pdf', 'kicadSymbolki_keywords': 'Reflective Optical Sensor Opto', 'kicadSymbolki_description': 'Subminiature Reflective Optical Sensor, DIP-like THT-package', 'kicadSymbolki_fp_filters': 'Everlight*ITR8307F43*'}])
    newPart['name'].append('BPR-105F')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

