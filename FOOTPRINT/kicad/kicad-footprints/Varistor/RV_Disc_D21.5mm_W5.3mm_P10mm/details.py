
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Varistor"
    oIndex = "RV_Disc_D21.5mm_W5.3mm_P10mm"
    hexID = "FZKVRVDISCD215W53P1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RV_Disc_D21.5mm_W5.3mm_P10mm', 'description': 'Varistor, diameter 21.5mm, width 5.3mm, pitch 10mm', 'tags': 'varistor SIOV', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Varistor.3dshapes/RV_Disc_D21.5mm_W5.3mm_P10mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Varistor : RV_Disc_D21.5mm_W5.3mm_P10mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

