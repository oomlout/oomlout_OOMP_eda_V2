
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "Allegro_QSOP-24_3.9x8.7mm_P0.635mm"
    hexID = "FZKSENCURRENTALLEGROQS2439X87P635"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Allegro_QSOP-24_3.9x8.7mm_P0.635mm', 'description': 'Allegro Microsystems 24-Lead Plastic Shrink Small Outline Narrow Body Body [QSOP] (http://www.allegromicro.com/~/media/Files/Datasheets/ACS726-Datasheet.ashx?la=en)', 'tags': 'Allegro QSOP 0.635', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/QSOP-24_3.9x8.7mm_P0.635mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Current : Allegro_QSOP-24_3.9x8.7mm_P0.635mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

