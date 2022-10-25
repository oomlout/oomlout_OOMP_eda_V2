
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "Diodes_SIP-3_4.1x1.5mm_P2.65mm"
    hexID = "FZKSENCURRENTDIODESSIP341X15P265"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diodes_SIP-3_4.1x1.5mm_P2.65mm', 'description': 'Diodes SIP-3 Ammo Pack, 2.65mm Pitch (https://www.diodes.com/assets/Package-Files/SIP-3-Ammo-Pack.pdf)', 'tags': 'Diodes SIP-3 Ammo Pack', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/Diodes_SIP-3_4.1x1.5mm_P2.65mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Current : Diodes_SIP-3_4.1x1.5mm_P2.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

