
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "LEM_HX50-P-SP2"
    hexID = "FZKSENCURRENTLEMHX5PSP2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LEM_HX50-P-SP2', 'description': 'LEM HX50-P-SP2 hall effect current transducer (https://www.lem.com/sites/default/files/products_datasheets/hx%203_50-p_sp2_e%20v07.pdf)', 'tags': 'hall current', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/LEM_HX50-P-SP2.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Current : LEM_HX50-P-SP2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

