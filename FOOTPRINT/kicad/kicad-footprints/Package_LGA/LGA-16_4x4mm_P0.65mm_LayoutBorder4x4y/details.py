
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LGA"
    oIndex = "LGA-16_4x4mm_P0.65mm_LayoutBorder4x4y"
    hexID = "FZKLGALGA164X4P65LAYOUTBORDER4X4Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LGA-16_4x4mm_P0.65mm_LayoutBorder4x4y', 'description': 'LGA, 16 Pin (http://www.st.com/resource/en/datasheet/l3gd20.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LGA NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/LGA-16_4x4mm_P0.65mm_LayoutBorder4x4y.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_LGA : LGA-16_4x4mm_P0.65mm_LayoutBorder4x4y')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

