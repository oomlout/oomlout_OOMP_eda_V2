
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "UDFN-10_1.35x2.6mm_P0.5mm"
    hexID = "FZKDFNUDFN1135X26P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UDFN-10_1.35x2.6mm_P0.5mm', 'description': 'http://www.st.com/content/ccc/resource/technical/document/datasheet/f2/11/8a/ed/40/31/40/56/DM00088292.pdf/files/DM00088292.pdf/jcr:content/translations/en.DM00088292.pdf', 'tags': 'UDFN 0.5 uQFN', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UDFN-10_1.35x2.6mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'oval'}})
    newPart['name'].append('Package_DFN_QFN : UDFN-10_1.35x2.6mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

