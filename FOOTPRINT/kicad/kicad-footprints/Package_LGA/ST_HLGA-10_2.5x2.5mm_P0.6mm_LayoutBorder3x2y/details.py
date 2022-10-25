
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LGA"
    oIndex = "ST_HLGA-10_2.5x2.5mm_P0.6mm_LayoutBorder3x2y"
    hexID = "FZKLGASTHLGA125X25P6LAYOUTBORDER3X2Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ST_HLGA-10_2.5x2.5mm_P0.6mm_LayoutBorder3x2y', 'description': 'ST  HLGA, 10 Pin (https://www.st.com/resource/en/datasheet/lps25hb.pdf#page=46), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'ST HLGA NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/ST_HLGA-10_2.5x2.5mm_P0.6mm_LayoutBorder3x2y.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_LGA : ST_HLGA-10_2.5x2.5mm_P0.6mm_LayoutBorder3x2y')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

