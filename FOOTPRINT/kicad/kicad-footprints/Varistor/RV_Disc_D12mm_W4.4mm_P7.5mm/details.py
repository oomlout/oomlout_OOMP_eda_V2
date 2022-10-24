
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Varistor"
    oIndex = "RV_Disc_D12mm_W4.4mm_P7.5mm"
    hexID = "FZKVRVDISCD12W44P75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RV_Disc_D12mm_W4.4mm_P7.5mm', 'description': 'Varistor, diameter 12mm, width 4.4mm, pitch 7.5mm', 'tags': 'varistor SIOV', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Varistor.3dshapes/RV_Disc_D12mm_W4.4mm_P7.5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Varistor : RV_Disc_D12mm_W4.4mm_P7.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

