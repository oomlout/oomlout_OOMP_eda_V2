
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Humidity"
    oIndex = "Sensirion_DFN-4-1EP_2x2mm_P1mm_EP0.7x1.6mm"
    hexID = "FZKSENHUMIDITYSENSIRIONDFN41EP2X2P1EP7X16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Sensirion_DFN-4-1EP_2x2mm_P1mm_EP0.7x1.6mm', 'description': 'DFN, 4 Pin (https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/0_Datasheets/Humidity/Sensirion_Humidity_Sensors_SHTC3_Datasheet.pdf)', 'tags': 'Sensirion DFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Humidity.3dshapes/Sensirion_DFN-4-1EP_2x2mm_P1mm_EP0.7x1.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Sensor_Humidity : Sensirion_DFN-4-1EP_2x2mm_P1mm_EP0.7x1.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

