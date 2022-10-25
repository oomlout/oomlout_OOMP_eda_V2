
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "AKM_CQ_7S"
    hexID = "FZKSENCURRENTAKMCQ7S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'AKM_CQ_7S', 'description': 'AKM Current Sensor, 7 pin, SMD (http://www.akm.com/akm/en/file/datasheet/CQ-236B.pdf)', 'tags': 'akm current sensor smd', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/AKM_CQ_7S.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Current : AKM_CQ_7S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

