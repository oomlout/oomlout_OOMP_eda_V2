
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "WLCSP-81_4.41x3.76mm_P0.4mm"
    hexID = "FZKCSPWLCSP81441X376P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLCSP-81_4.41x3.76mm_P0.4mm', 'description': 'WLCSP-81, 9x9, 0.4mm Pitch, http://www.st.com/content/ccc/resource/technical/document/technical_note/92/30/3c/a1/4c/bb/43/6f/DM00103228.pdf/files/DM00103228.pdf/jcr:content/translations/en.DM00103228.pdf', 'tags': 'WLCSP ST', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-81_4.41x3.76mm_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : WLCSP-81_4.41x3.76mm_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

