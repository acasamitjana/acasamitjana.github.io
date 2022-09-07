---
title: Synth-by-Reg (SbR). Contrastive learning for synthesis-based registration of paired images
collection: publications
type: conference
permalink: /publications/2021-SASHIMI-SbR
date: 2021-9-27
venue: International Workshop on Simulation and Synthesis in Medical Imaging, SASHIMI (MICCAI-21 Satellite Event)
paperurl: 'https://link.springer.com/chapter/10.1007/978-3-030-87592-3_5'
authors: <b>Adrià Casamitjana</b>, Matteo Mancini, Juan Eugenio Iglesias
pdflink: https://arxiv.org/pdf/2107.14449.pdf
citationlink: https://scholar.google.com/citations?view_op=view_citation&hl=ca&user=phHLLH0AAAAJ&sortby=pubdate&citation_for_view=phHLLH0AAAAJ:4TOpqqG69KYC
---

## Abstract
Nonlinear inter-modality registration is often challenging due
to the lack of objective functions that are good proxies for alignment.
Here we propose a synthesis-by-registration method to convert this prob-
lem into an easier intra-modality task. We introduce a registration loss
for weakly supervised image translation between domains that does not
require perfectly aligned training data. This loss capitalises on a regis-
tration U-Net with frozen weights, to drive a synthesis CNN towards the
desired translation. We complement this loss with a structure preserv-
ing constraint based on contrastive learning, which prevents blurring and
content shifts due to overfitting. We apply this method to the registration
of histological sections to MRI slices, a key step in 3D histology recon-
struction. Results on two public datasets show improvements over regis-
tration based on mutual information (13% reduction in landmark error)
and synthesis-based algorithms such as CycleGAN (11% reduction), and
are comparable to registration with label supervision. Code and data are
publicly available at https://github.com/acasamitjana/SynthByReg.
