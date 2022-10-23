
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "NCP163AFCT300T2G"
    hexID = "SZKREGULATORLINEARNCP163AFCT3T2G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCP163AFCS120T2G', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP163AFCT300T2G', 'kicadSymbolFootprint': 'Package_CSP:WLCSP-4_0.64x0.64mm_P0.35mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pdf/datasheet/ncp163-d.pdf', 'kicadSymbolki_keywords': 'LDO regulator voltage', 'kicadSymbolki_description': '250mA low-noise LDO, 2.2V-5.5V input, 3.0V output, WLCSP-4', 'kicadSymbolki_fp_filters': 'WLCSP*'}])
    newPart['name'].append('NCP163AFCT300T2G')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

