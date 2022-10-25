
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LGA"
    oIndex = "Kionix_LGA-12_2x2mm_P0.5mm_LayoutBorder2x4y"
    hexID = "FZKLGAKIONIXLGA122X2P5LAYOUTBORDER2X4Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Kionix_LGA-12_2x2mm_P0.5mm_LayoutBorder2x4y', 'description': 'Kionix  LGA, 12 Pin (http://kionixfs.kionix.com/en/document/TN008-PCB-Design-Guidelines-for-2x2-LGA-Sensors.pdf#page=4), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Kionix LGA NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/Kionix_LGA-12_2x2mm_P0.5mm_LayoutBorder2x4y.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_LGA : Kionix_LGA-12_2x2mm_P0.5mm_LayoutBorder2x4y')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

