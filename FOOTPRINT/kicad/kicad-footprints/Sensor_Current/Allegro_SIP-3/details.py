
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "Allegro_SIP-3"
    hexID = "FZKSENCURRENTALLEGROSIP3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Allegro_SIP-3', 'description': 'Allegro Microsystems SIP-3, 1.27mm Pitch (http://www.allegromicro.com/~/media/Files/Datasheets/A1369-Datasheet.ashx)', 'tags': 'Allegro SIP-3', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/Allegro_SIP-3.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Current : Allegro_SIP-3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

