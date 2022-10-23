
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Filter"
    oIndex = "Filter_Schaffner_FN405"
    hexID = "FZKFILFILSCHAFFNERFN45"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Filter_Schaffner_FN405', 'description': 'Compact PCB mounting EMI filter (https://www.schaffner.com/de/produkte/download/product/datasheet/fn-405-pcb-mounting-filter/)', 'tags': 'EMI filter', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Filter.3dshapes/Filter_Schaffner_FN405.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Filter : Filter_Schaffner_FN405')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

