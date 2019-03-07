combine stack and app for cc2650
====================================
TI examles compiling two program separatly (stack and app program)
in Code Composer Studio setting(Properties->Build->Steps) 
needs set for build bin file 

${CG_TOOL_HEX} -order MS --memwidth=8 --romwidth=8 --intel -o      ${ProjName}.hex ${ProjName}.out

"${CCS_INSTALL_ROOT}/utils/tiobj2bin/tiobj2bin" "${BuildArtifactFileName}" "${BuildArtifactFileBaseName}.bin" "${CG_TOOL_ROOT}/bin/armofd" "${CG_TOOL_ROOT}/bin/armhex" "${CCS_INSTALL_ROOT}/utils/tiobj2bin/mkhex4bin"

For correctly work we should have both in chip, have to use

python add_stack.py -a simple_peripheral_cc2650lp_app.bin -s simple_peripheral_cc2650lp_stack.bin

and them use standart utility for flash new file on device

python cc2538-bsl.py -p COM11 -e -w -v simple_peripheral_cc2650lp_app_with_stack.bin




