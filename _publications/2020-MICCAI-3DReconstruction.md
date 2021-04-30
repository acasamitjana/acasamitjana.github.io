---
title: 3D Reconstruction and Segmentation of Dissection Photographs for MRI-Free Neuropathology
collection: publications
type: conference
permalink: /publications/2020-MICCAI-3DReconstruction
date: 20120-09-29
venue: International Conference on Medical Image Computing and Computer-Assisted Intervention
paperurl: https://link.springer.com/chapter/10.1007/978-3-030-59722-1_20
authors: Henry F. J. Tregidgo, <b>Adrià Casamitjana</b>, Caitlin S. Latimer, Mitchell D. Kilgore, Eleanor Robinson, Emily Blackburn, Koen Van Leemput, Bruce Fischl, Adrian V. Dalca, Christine L. Mac Donald, C. Dirk Keene, Juan Eugenio Iglesias
pdflink: https://arxiv.org/pdf/2009.05596.pdf
citationlink: https://scholar.google.com/scholar?oi=bibs&hl=ca&cluster=9790302808436967267
---

## Abstract
Neuroimaging to neuropathology correlation (NTNC) promis-es to enable the transfer of microscopic signatures of pathology to in vivo imaging with MRI, ultimately enhancing clinical care. NTNC traditionally requires a volumetric MRI scan, acquired either ex vivo or a short time prior to death. Unfortunately, ex vivo MRI is difficult and costly, and recent premortem scans of sufficient quality are seldom available. To bridge this gap, we present methodology to 3D reconstruct and segment full brain image volumes from brain dissection photographs, which are routinely acquired at many brain banks and neuropathology departments. The 3D reconstruction is achieved via a joint registration framework, which uses a reference volume other than MRI. This volume may represent either the sample at hand (e.g., a surface 3D scan) or the general population (a probabilistic atlas). In addition, we present a Bayesian method to segment the 3D reconstructed photographic volumes into 36 neuroanatomical structures, which is robust to nonuniform brightness within and across photographs. We evaluate our methods on a dataset with 24 brains, using Dice scores and volume correlations. The results show that dissection photography is a valid replacement for ex vivo MRI in many volumetric analyses, opening an avenue for MRI-free NTNC, including retrospective data. The code is available at https://github.com/htregidgo/DissectionPhotoVolumes.
