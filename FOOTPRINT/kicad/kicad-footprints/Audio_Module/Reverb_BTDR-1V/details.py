
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Audio_Module"
    oIndex = "Reverb_BTDR-1V"
    hexID = "FZKAREVERBBTDR1V"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Reverb_BTDR-1V', 'description': 'Digital Reverberation Unit, http://www.belton.co.kr/inc/downfile.php?seq=17&file=pdf (footprint from http://www.uk-electronic.de/PDF/BTDR-1.pdf)', 'tags': 'audio belton reverb', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Audio_Module.3dshapes/Reverb_BTDR-1V.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Audio_Module : Reverb_BTDR-1V')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

