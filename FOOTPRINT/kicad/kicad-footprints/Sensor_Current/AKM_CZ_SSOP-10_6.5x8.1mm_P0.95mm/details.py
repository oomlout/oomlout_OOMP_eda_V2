
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "AKM_CZ_SSOP-10_6.5x8.1mm_P0.95mm"
    hexID = "FZKSENCURRENTAKMCZSS165X81P95"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'AKM_CZ_SSOP-10_6.5x8.1mm_P0.95mm', 'description': 'AKM CZ-381x current sensor, 6.5x8.1mm body, 0.95mm pitch (http://www.akm.com/akm/en/product/detail/0009/)', 'tags': 'akm cz-381x 10', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/AKM_CZ_SSOP-10_6.5x8.1mm_P0.95mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Current : AKM_CZ_SSOP-10_6.5x8.1mm_P0.95mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

