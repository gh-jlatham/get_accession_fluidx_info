# get_accession_fluidx_info
Get Fluid-X plate/tube/well from Accession ID (or vice versa starting with Fluid-X tube)

Instructions:

1. Clone this repo:
```bash
mkdir -p ~/src
cd ~/src
git clone git@github.com:lspurkaGH/get_accession_fluidx_info.git
```

2. Install python3.  (If you've already done this, skip to step 3.)
In terminal paste:

```bash
# Code from @Carlo:
#Python 3.6
INSTALL_DIR=~/
if [ $(uname) == "Darwin" ]; then
	curl https://repo.continuum.io/miniconda/Miniconda3-4.5.4-MacOSX-x86_64.sh > ${INSTALL_DIR}/Miniconda3-4.5.4-MacOSX-x86_64.sh &&
	bash ${INSTALL_DIR}/Miniconda3-4.5.4-MacOSX-x86_64.sh -b -p ${INSTALL_DIR}/miniconda3/
	rm ${INSTALL_DIR}/Miniconda3-4.5.4-MacOSX-x86_64.sh
else
	wget https://repo.continuum.io/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh -P ${INSTALL_DIR} &&
	bash ${INSTALL_DIR}/Miniconda3-4.5.4-Linux-x86_64.sh -b -p ${INSTALL_DIR}/miniconda3/
	rm ${INSTALL_DIR}/Miniconda3-4.5.4-Linux-x86_64.sh
fi
${INSTALL_DIR}/miniconda3/bin/conda env create -f ~/src/get_accession_fluidx_info/py3.yaml
```

3. activate python3 virtual env:
```bash
source ~/miniconda3/bin/activate py3
```
You will know that your virtual env is active if you see "(py#)" of your line at the beginning

4. Connect to


