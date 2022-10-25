
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Humidity"
    oIndex = "Sensirion_DFN-8-1EP_2.5x2.5mm_P0.5mm_EP1.1x1.7mm"
    hexID = "FZKSENHUMIDITYSENSIRIONDFN81EP25X25P5EP11X17"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Sensirion_DFN-8-1EP_2.5x2.5mm_P0.5mm_EP1.1x1.7mm', 'description': 'Sensirion DFN-8 SHT3x-DIS (https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/2_Humidity_Sensors/Datasheets/Sensirion_Humidity_Sensors_SHT3x_Datasheet_digital.pdf)', 'tags': 'sensirion dfn nolead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Humidity.3dshapes/Sensirion_DFN-8-1EP_2.5x2.5mm_P0.5mm_EP1.1x1.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Sensor_Humidity : Sensirion_DFN-8-1EP_2.5x2.5mm_P0.5mm_EP1.1x1.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

