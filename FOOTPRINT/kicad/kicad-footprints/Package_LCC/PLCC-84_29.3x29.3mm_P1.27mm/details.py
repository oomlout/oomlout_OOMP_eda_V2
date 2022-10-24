
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LCC"
    oIndex = "PLCC-84_29.3x29.3mm_P1.27mm"
    hexID = "FZKLCCPLCC84293X293P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PLCC-84_29.3x29.3mm_P1.27mm', 'description': 'PLCC, 84 Pin (http://www.microsemi.com/index.php?option=com_docman&task=doc_download&gid=131095), generated with kicad-footprint-generator ipc_plcc_jLead_generator.py', 'tags': 'PLCC LCC', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LCC.3dshapes/PLCC-84_29.3x29.3mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_LCC : PLCC-84_29.3x29.3mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

