
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "MSOP-10-1EP_3x3mm_P0.5mm_EP1.73x1.98mm"
    hexID = "FZKSOMS11EP3X3P5EP173X198"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MSOP-10-1EP_3x3mm_P0.5mm_EP1.73x1.98mm', 'description': 'MSOP, 10 Pin (www.allegromicro.com/~/media/Files/Datasheets/A4952-3-Datasheet.ashx?la=en#page=10), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'MSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/MSOP-10-1EP_3x3mm_P0.5mm_EP1.73x1.98mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : MSOP-10-1EP_3x3mm_P0.5mm_EP1.73x1.98mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

