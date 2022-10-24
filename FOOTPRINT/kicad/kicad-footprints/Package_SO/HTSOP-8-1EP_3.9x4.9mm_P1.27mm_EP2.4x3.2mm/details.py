
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.4x3.2mm"
    hexID = "FZKSOHTS81EP39X49P127EP24X32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.4x3.2mm', 'description': 'HTSOP, 8 Pin (https://media.digikey.com/pdf/Data%20Sheets/Rohm%20PDFs/BD9G341EFJ.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'HTSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.4x3.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.4x3.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

