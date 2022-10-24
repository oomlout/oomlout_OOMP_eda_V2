
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_SeikoEpson_SG8002JC-4Pin_10.5x5.0mm_HandSoldering"
    hexID = "FZKOCSOCSSMSEIKOEPSONSG82JC4PIN15X5HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_SeikoEpson_SG8002JC-4Pin_10.5x5.0mm_HandSoldering', 'description': 'SMD Crystal Oscillator Seiko Epson SG-8002JC https://support.epson.biz/td/api/doc_check.php?mode=dl&lang=en&Parts=SG-8002DC, hand-soldering, 10.5x5.0mm^2 package', 'tags': 'SMD SMT crystal oscillator hand-soldering', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_SeikoEpson_SG8002JC-4Pin_10.5x5.0mm_HandSoldering.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_SeikoEpson_SG8002JC-4Pin_10.5x5.0mm_HandSoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

