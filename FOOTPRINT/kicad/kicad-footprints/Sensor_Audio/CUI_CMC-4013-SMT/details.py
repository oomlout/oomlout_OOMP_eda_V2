
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Audio"
    oIndex = "CUI_CMC-4013-SMT"
    hexID = "FZKSENAUDIOCUICMC413S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CUI_CMC-4013-SMT', 'description': 'Omnidirectional, -42dB, reflowable, electret condenser microphone https://www.cuidevices.com/product/resource/cmc-4013-smt-tr.pdf', 'tags': 'Microphone CUI ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Audio.3dshapes/CUI_CMC-4013-SMT.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Sensor_Audio : CUI_CMC-4013-SMT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

