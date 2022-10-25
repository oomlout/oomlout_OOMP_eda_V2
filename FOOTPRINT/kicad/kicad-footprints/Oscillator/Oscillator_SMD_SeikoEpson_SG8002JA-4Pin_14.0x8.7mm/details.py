
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_SeikoEpson_SG8002JA-4Pin_14.0x8.7mm"
    hexID = "FZKOCSOCSSMSEIKOEPSONSG82JA4PIN14X87"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_SeikoEpson_SG8002JA-4Pin_14.0x8.7mm', 'description': 'SMD Crystal Oscillator Seiko Epson SG-8002JA https://support.epson.biz/td/api/doc_check.php?mode=dl&lang=en&Parts=SG-8002DC, 14.0x8.7mm^2 package', 'tags': 'SMD SMT crystal oscillator', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_SeikoEpson_SG8002JA-4Pin_14.0x8.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_SeikoEpson_SG8002JA-4Pin_14.0x8.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

