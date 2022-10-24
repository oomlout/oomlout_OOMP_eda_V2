
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSO-4_6.7x5.1mm_P2.54mm_Clearance8mm"
    hexID = "FZKSOSSO467X51P254CLEARANCE8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSO-4_6.7x5.1mm_P2.54mm_Clearance8mm', 'description': '4-Lead Plastic Stretched Small Outline (SSO/Stretched SO), see https://www.vishay.com/docs/84299/vor1142b4.pdf', 'tags': 'SSO Stretched SO SOIC 2.54', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSO-4_6.7x5.1mm_P2.54mm_Clearance8mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SSO-4_6.7x5.1mm_P2.54mm_Clearance8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

