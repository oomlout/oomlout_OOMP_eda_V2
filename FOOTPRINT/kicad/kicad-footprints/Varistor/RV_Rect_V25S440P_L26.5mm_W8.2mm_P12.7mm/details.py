
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Varistor"
    oIndex = "RV_Rect_V25S440P_L26.5mm_W8.2mm_P12.7mm"
    hexID = "FZKVRVRECTV25S44PL265W82P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RV_Rect_V25S440P_L26.5mm_W8.2mm_P12.7mm', 'description': 'Varistor, V25S440P, https://www.littelfuse.com/media?resourcetype=datasheets&itemid=b410c42c-51d1-460e-b1d9-d105d93c9679&filename=littelfuse-varistor-ultramov25s-datasheet', 'tags': 'varistor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Varistor.3dshapes/RV_Rect_V25S440P_L26.5mm_W8.2mm_P12.7mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Varistor : RV_Rect_V25S440P_L26.5mm_W8.2mm_P12.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

