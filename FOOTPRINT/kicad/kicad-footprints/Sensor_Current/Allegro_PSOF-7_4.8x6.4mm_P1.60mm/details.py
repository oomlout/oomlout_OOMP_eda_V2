
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "Allegro_PSOF-7_4.8x6.4mm_P1.60mm"
    hexID = "FZKSENCURRENTALLEGROPSOF748X64P16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Allegro_PSOF-7_4.8x6.4mm_P1.60mm', 'description': 'Allegro Microsystems PSOF-7, 4.8x6.4mm Body, 1.60mm Pitch (http://www.allegromicro.com/~/media/Files/Datasheets/ACS780-Datasheet.ashx)', 'tags': 'Allegro PSOF-7', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/Allegro_PSOF-7_4.8x6.4mm_P1.60mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Current : Allegro_PSOF-7_4.8x6.4mm_P1.60mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

