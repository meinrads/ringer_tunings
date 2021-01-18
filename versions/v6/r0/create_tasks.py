import os
basepath = os.getcwd()


path = basepath + '/Zee/v6/r0'


command = """maestro.py task create \
  -v {PATH} \
  -t user.jodafons.mc15_13TeV.sgn.probes_lhmedium_Zee.bkg.Truth.JF17.oldgrid.v7_et{ET}_eta{ETA}.r0 \
  -c user.jodafons.job_config.Zee_v6.n2to5.10sorts.10inits.r0 \
  -d user.jodafons.mc15_13TeV.sgn.probes_lhmedium_Zee.bkg.Truth.JF17.oldgrid_et{ET}_eta{ETA}.npz \
  --sd "{REF}" \
  --exec "run_tuning.py -c %IN -d %DATA -r %REF -v %OUT -b zee -t v6 -p r0 \
  --queue "gpu" """


os.makedirs(path)

for et in range(5):
    for eta in range(4):
        ref = "{'%%REF':'user.jodafons.mc15_13TeV.sgn.probes_lhmedium_Zee.bkg.Truth.JF17.oldgrid_et{ET}_eta{ETA}.ref.pic.gz'}"%(et,eta)
        cmd = command.format(ET=et,ETA=eta,REF=ref,PATH=path)
        print(cmd)
        os.system(cmd)


