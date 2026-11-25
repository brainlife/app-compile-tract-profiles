<h1 align="center">Compile tract profiles to a summary table</h1>

<p align="center">
  One long-format csv (subject, tract, node, one column per measure) from a subject's per-tract profile files, ready for group analysis and machine learning.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.384"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.384-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Compiles the per-tract profile csv files of one subject's tractprofile output into a single long-format csv (subject, tract, node, mean of each measure) with pandas, for group analysis and machine learning.**

Reads every *_profiles.csv in the tractprofile directory, keeps the *_mean columns, and writes output_FiberStats.csv with one row per tract and node and one column per diffusion measure, labelled with the subject ID from the input metadata. Use it to turn tract profiles into a tidy table; the README mentions tracts.csv but the code writes output_FiberStats.csv.

| | |
|---|---|
| **Inputs** | `neuro/tractprofile-deprecated` |
| **Outputs** | `neuro/tractmeasures` |
| **Container** | `brainlife/freesurfer-stats:1.2` |
| **Resources** | 4 CPUs · 29 GB memory |
| **Run it** | [doi.org/10.25663/brainlife.app.384](https://doi.org/10.25663/brainlife.app.384) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `profiles` | `neuro/tractprofile-deprecated` | yes | The path to the top directory containing the tract profile .csv files |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `tractmeasures` | `neuro/tractmeasures` | The output is a combined version of the inputted .csvs file into a single .csv file analyses |

<!-- brainlife-app:end -->

## Running the App

The App reads every `*_profiles.csv` file in the input tract-profile directory, keeps the `*_mean` columns (one per diffusion measure), and stacks them into a single table with one row per tract and node, labelled with the subject ID from the input metadata.

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.384](https://doi.org/10.25663/brainlife.app.384), choose a tract-profile dataset (`neuro/tractprofile-deprecated`) from your project and press **Execute**. The table is archived to your project as a `neuro/tractmeasures` dataset tagged `profiles`, which you can download or combine across subjects for group statistics.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/). The App runs `generateCSV.py` (Python 3, pandas, NumPy) inside the `brainlife/freesurfer-stats:1.2` container.

1. Clone this repository and check out the registered version: `git checkout v1.1`.
2. Create `config.json` with the path to the directory of profile csv files and the subject ID (read from `_inputs[0].meta.subject`):

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

3. Run the App:

   ```bash
   ./main
   ```

### Sample data

Download a tract-profile dataset from brainlife.io with the [brainlife CLI](https://github.com/brainlife/cli):

```bash
npm install -g brainlife
bl login
mkdir input
bl dataset download <dataset id>
```

## Outputs

```text
tractmeasures/
└── output_FiberStats.csv   columns: subjectID, structureID, nodeID, then one column per measure (e.g. fa, md, …)
```

`structureID` is the profile file name without `_profiles.csv` and with underscores removed. Rows are sorted by tract and node.

The `master` branch is a later revision that writes `tractmeasures/tracts.csv` instead; the App on brainlife.io runs `v1.1` and writes `output_FiberStats.csv`.

## Troubleshooting

- **`stats computations failed somewhere. please check logs and derivatives`**: the csv was not written. Check that the profiles directory contains `*_profiles.csv` files with `*_mean` columns, and that `config.json` has a subject under `_inputs[0].meta.subject`.

## Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Yeatman JD, Dougherty RF, Myall NJ, Wandell BA, Feldman HM. Tract profiles of white matter properties: automating fiber-tract quantification. *PLoS ONE* 7(11):e49790 (2012). [doi:10.1371/journal.pone.0049790](https://doi.org/10.1371/journal.pone.0049790)
- Compile tract profiles to summary structure. brainlife.io App. [doi:10.25663/brainlife.app.384](https://doi.org/10.25663/brainlife.app.384)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Brad Caron

**Contributors:** Soichi Hayashi, Franco Pestilli

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## License

[MIT](LICENSE).
