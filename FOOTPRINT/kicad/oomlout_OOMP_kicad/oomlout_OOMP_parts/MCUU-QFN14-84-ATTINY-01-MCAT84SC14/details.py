
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "MCUU-QFN14-84-ATTINY-01-MCAT84SC14"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSMCUUQFN1484ATTINY1MCAT84SC14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MCUU-QFN14-84-ATTINY-01-MCAT84SC14', 'description': 'hexID: MCAT84SC14; QFN, 20 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/doc2535.pdf#page=164), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('oomlout_OOMP_parts : MCUU-QFN14-84-ATTINY-01-MCAT84SC14')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

