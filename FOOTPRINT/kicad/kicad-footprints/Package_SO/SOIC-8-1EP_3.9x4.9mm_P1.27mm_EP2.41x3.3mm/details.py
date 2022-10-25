
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.3mm"
    hexID = "FZKSOSOIC81EP39X49P127EP241X33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.3mm', 'description': 'SOIC, 8 Pin (http://www.allegromicro.com/~/media/Files/Datasheets/A4950-Datasheet.ashx#page=8), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SOIC SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.3mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

