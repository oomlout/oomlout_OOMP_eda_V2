
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "Allegro_QFN-12-10-1EP_3x3mm_P0.5mm"
    hexID = "FZKSENCURRENTALLEGROQFN1211EP3X3P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Allegro_QFN-12-10-1EP_3x3mm_P0.5mm', 'description': 'Allegro Microsystems 12-Lead (10-Lead Populated) Quad Flat Pack, 3x3mm Body, 0.5mm Pitch (http://www.allegromicro.com/~/media/Files/Datasheets/ACS711-Datasheet.ashx)', 'tags': 'Allegro QFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/Allegro_QFN-12-10-1EP_3x3mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Current : Allegro_QFN-12-10-1EP_3x3mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

