
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LGA"
    oIndex = "LGA-14_2x2mm_P0.35mm_LayoutBorder3x4y"
    hexID = "FZKLGALGA142X2P35LAYOUTBORDER3X4Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LGA-14_2x2mm_P0.35mm_LayoutBorder3x4y', 'description': 'LGA, 14 Pin (http://www.st.com/resource/en/datasheet/lis2dh.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LGA NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/LGA-14_2x2mm_P0.35mm_LayoutBorder3x4y.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_LGA : LGA-14_2x2mm_P0.35mm_LayoutBorder3x4y')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

