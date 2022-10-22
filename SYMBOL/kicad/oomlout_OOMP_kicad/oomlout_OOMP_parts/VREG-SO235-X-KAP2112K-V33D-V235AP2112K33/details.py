
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "VREG-SO235-X-KAP2112K-V33D-V235AP2112K33"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSVREGSO235XKAP2112KV33DV235AP2112K33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VREG-SO235-X-KAP2112K-V33D-V235AP2112K33', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:VREG-SO235-X-KAP2112K-V33D-V235AP2112K33', 'kicadSymbolDatasheet': 'oom.lt/V235AP2112K33', 'kicadSymbolki_keywords': 'linear regulator ldo fixed positive', 'kicadSymbolki_description': 'hexID: V235AP2112K33;600mA low dropout linear regulator, with enable pin, 3.8V-6V input voltage range, 3.3V fixed positive output, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23?5*'}])
    newPart['name'].append('VREG-SO235-X-KAP2112K-V33D-V235AP2112K33')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

