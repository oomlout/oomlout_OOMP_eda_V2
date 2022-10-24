
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "AKM_CQ_VSOP-24_5.6x7.9mm_P0.65mm"
    hexID = "FZKSENCURRENTAKMCQVS2456X79P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'AKM_CQ_VSOP-24_5.6x7.9mm_P0.65mm', 'description': 'AKM VSOP-24 current sensor, 5.6x7.9mm body, 0.65mm pitch (http://www.akm.com/akm/en/file/datasheet/CQ-330J.pdf)', 'tags': 'akm vsop 24', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/AKM_CQ_VSOP-24_5.6x7.9mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Current : AKM_CQ_VSOP-24_5.6x7.9mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

