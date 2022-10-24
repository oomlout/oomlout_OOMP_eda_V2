
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SO-4_4.4x3.9mm_P2.54mm"
    hexID = "FZKSOSO444X39P254"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SO-4_4.4x3.9mm_P2.54mm', 'description': 'SO, 4 Pin (https://toshiba.semicon-storage.com/info/docget.jsp?did=10047&prodName=TLP3123), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SO SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SO-4_4.4x3.9mm_P2.54mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SO-4_4.4x3.9mm_P2.54mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

