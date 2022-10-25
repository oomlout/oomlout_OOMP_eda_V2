
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "HVSOF6"
    hexID = "FZKPACKAGETOSOTSMHVSOF6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HVSOF6', 'description': 'HVSOF6, http://rohmfs.rohm.com/en/techdata_basic/ic/package/hvsof6_1-e.pdf, http://rohmfs.rohm.com/en/products/databook/datasheet/ic/audio_video/video_amplifier/bh76106hfv-e.pdf', 'tags': 'HVSOF6', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/HVSOF6.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_SMD : HVSOF6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

