
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LGA"
    oIndex = "LGA-16_3x3mm_P0.5mm_LayoutBorder3x5y"
    hexID = "FZKLGALGA163X3P5LAYOUTBORDER3X5Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LGA-16_3x3mm_P0.5mm_LayoutBorder3x5y', 'description': 'LGA, 16 Pin (http://www.st.com/resource/en/datasheet/lis331hh.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LGA NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/LGA-16_3x3mm_P0.5mm_LayoutBorder3x5y.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_LGA : LGA-16_3x3mm_P0.5mm_LayoutBorder3x5y')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

