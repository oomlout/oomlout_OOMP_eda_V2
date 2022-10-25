
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LGA"
    oIndex = "NXP_LGA-8_3x5mm_P1.25mm_H1.2mm"
    hexID = "FZKLGANXPLGA83X5P125H12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'NXP_LGA-8_3x5mm_P1.25mm_H1.2mm', 'description': 'NXP  LGA, 8 Pin (https://www.nxp.com/docs/en/data-sheet/MPL115A1.pdf#page=15), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'NXP LGA NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/NXP_LGA-8_3x5mm_P1.25mm_H1.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_LGA : NXP_LGA-8_3x5mm_P1.25mm_H1.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

