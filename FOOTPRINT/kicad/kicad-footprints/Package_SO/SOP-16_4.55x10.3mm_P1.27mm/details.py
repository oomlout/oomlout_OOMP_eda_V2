
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SOP-16_4.55x10.3mm_P1.27mm"
    hexID = "FZKSOS16455X13P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOP-16_4.55x10.3mm_P1.27mm', 'description': 'SOP, 16 Pin (https://toshiba.semicon-storage.com/info/docget.jsp?did=12855&prodName=TLP290-4), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOP-16_4.55x10.3mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SOP-16_4.55x10.3mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

