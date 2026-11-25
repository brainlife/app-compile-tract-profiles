[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-brainlife.app.384-blue.svg)](https://doi.org/https://doi.org/10.25663/brainlife.app.384)

# Compile tract profile measures to a summary csv 

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

**Compiles the per-tract profile csv files of one subject's tractprofile output into a single long-format csv (subject, tract, node, mean of each measure) with pandas, for group analysis and machine learning.**

Reads every *_profiles.csv in the tractprofile directory, keeps the *_mean columns, and writes output_FiberStats.csv with one row per tract and node and one column per diffusion measure, labelled with the subject ID from the input metadata. Use it to turn tract profiles into a tidy table; the README mentions tracts.csv but the code writes output_FiberStats.csv.

Run it on brainlife.io: [https://doi.org/10.25663/brainlife.app.384](https://doi.org/10.25663/brainlife.app.384)

| Input | Datatype | Required | Description |
|---|---|---|---|
| `profiles` | `neuro/tractprofile-deprecated` | yes | The path to the top directory containing the tract profile .csv files |

| Output | Datatype | Description |
|---|---|---|
| `tractmeasures` | `neuro/tractmeasures` | The output is a combined version of the inputted .csvs file into a single .csv file analyses |

Runtime: container `brainlife/freesurfer-stats:1.2`; 4 CPUs; 29 GB memory.

<!-- brainlife-app:end -->

This app will the individual tract tract profiles csv's from the tractprofile dataype into a single summary csv for group analysis and machine learning. This app takes in a tractprofile datatype. The app will output a csv entitled 'tracts.csv' that can be used for group statistics and machine learning.

### Authors 

- Brad Caron (bacaron@iu.edu) 

### Contributors 

- Soichi Hayashi (hayashi@iu.edu)
- Franco Pestilli (frakkopesto@gmail.com)

### Funding 
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations 

Please cite the following articles when publishing papers that used data, code or other resources created by the brainlife.io community. 

Yeatman JD, Dougherty RF, Myall NJ, Wandell BA, Feldman HM (2012) Tract Profiles of White Matter Properties: Automating Fiber-Tract Quantification. PLoS ONE 7(11): e49790. https://doi.org/10.1371/journal.pone.0049790

Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). https://doi.org/10.1038/s41597-019-0073-y

## Running the App 

### On Brainlife.io 

You can submit this App online at [https://doi.org/10.25663/brainlife.app.384](https://doi.org/https://doi.org/10.25663/brainlife.app.384) via the 'Execute' tab. 

### Running Locally (on your machine) 

1. git clone this repo 

2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files. 

```json 
{ 
  "profiles": "./inputdata/profiles",
    "_inputs": [
        {
            "id": "profiles",
            "meta": {
                "subject": "subj001",
                "session": "1"
                    }
        }
    ]
} 
``` 

### Sample Datasets 

You can download sample datasets from Brainlife using [Brainlife CLI](https://github.com/brain-life/cli). 

```
npm install -g brainlife 
bl login 
mkdir input 
bl dataset download 
``` 

3. Launch the App by executing 'main' 

```bash 
./main 
``` 

## Output 

The main output is a folder called 'tractmeasures' with a csv with all of the tract profile information for each tract. 

#### Product.json 

The secondary output of this app is `product.json`. This file allows web interfaces, DB and API calls on the results of the processing. 

### Dependencies 

This App requires the following libraries when run locally. 

- singularity: https://singularity.lbl.gov/
- jsonlab: https://github.com/fangq/jsonlab.git
- python3: https://www.python.org/downloads/
- pandas: https://pandas.pydata.org/
