
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm"
    hexID = "FZKCSPLFCSP321EP5X5P5EP36X36"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm', 'description': 'LFCSP, 32 Pin (https://www.analog.com/media/en/technical-documentation/data-sheets/ADV7280.PDF#page=28), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LFCSP NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_CSP : LFCSP-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

