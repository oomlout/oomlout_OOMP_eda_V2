
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "Diodes_SIP-3_4.1x1.5mm_P1.27mm"
    hexID = "FZKSENCURRENTDIODESSIP341X15P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diodes_SIP-3_4.1x1.5mm_P1.27mm', 'description': 'Diodes SIP-3 Bulk Pack, 1.27mm Pitch (https://www.diodes.com/assets/Package-Files/SIP-3-Bulk-Pack.pdf)', 'tags': 'Diodes SIP-3 Bulk Pack', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/Diodes_SIP-3_4.1x1.5mm_P1.27mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Current : Diodes_SIP-3_4.1x1.5mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

