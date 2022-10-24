
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LGA"
    oIndex = "LGA-14_3x5mm_P0.8mm_LayoutBorder1x6y"
    hexID = "FZKLGALGA143X5P8LAYOUTBORDER1X6Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LGA-14_3x5mm_P0.8mm_LayoutBorder1x6y', 'description': 'LGA, 14 Pin (http://www.st.com/resource/en/datasheet/lsm303dlhc.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LGA NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/LGA-14_3x5mm_P0.8mm_LayoutBorder1x6y.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_LGA : LGA-14_3x5mm_P0.8mm_LayoutBorder1x6y')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

