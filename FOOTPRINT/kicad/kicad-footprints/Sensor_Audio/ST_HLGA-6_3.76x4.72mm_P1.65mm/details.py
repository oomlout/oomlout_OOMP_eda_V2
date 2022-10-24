
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Audio"
    oIndex = "ST_HLGA-6_3.76x4.72mm_P1.65mm"
    hexID = "FZKSENAUDIOSTHLGA6376X472P165"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ST_HLGA-6_3.76x4.72mm_P1.65mm', 'description': 'http://www.st.com/content/ccc/resource/technical/document/datasheet/group3/27/62/48/98/44/54/4d/36/DM00303211/files/DM00303211.pdf/jcr:content/translations/en.DM00303211.pdf', 'tags': 'HLGA Sensor Audio', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Audio.3dshapes/ST_HLGA-6_3.76x4.72mm_P1.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Sensor_Audio : ST_HLGA-6_3.76x4.72mm_P1.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

