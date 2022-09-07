---
title: Robust joint registration of multiple stains and MRI for multimodal 3D histology reconstruction. Application to the Allen human brain atlas
collection: publications
type: journal
permalink: /publications/2021-MedIA-Robust
date: 2021/4/30
venue: Medical Image Analysis
paperurl: ' https://www.sciencedirect.com/science/article/pii/S1361841521003108 '
authors: <b>Adrià Casamitjana</b>, Marco Lorenzi, Sebastiano Ferraris, Loc Peter, Marc Modat, Allison Stevens, Bruce Fischl, Tom Vercauteren, Juan Eugenio Iglesias
pdflink: https://arxiv.org/pdf/2104.14873.pdf
citationlink: https://scholar.google.com/scholar?oi=bibs&hl=ca&cluster=6938907588736391227
---

## Abstract
Joint registration of a stack of 2D histological sections to recover 3D structure (“3D histology reconstruction”) 
finds application in areas such as atlas building and validation of in vivo imaging. Straightforward pairwise 
registration of neighbouring sections yields smooth reconstructions but has well-known problems such as “banana effect” 
(straightening of curved structures) and “z-shift” (drift). While these problems can be alleviated with an external, 
linearly aligned reference (e.g., Magnetic Resonance (MR) images), registration is often inaccurate due to contrast 
differences and the strong nonlinear distortion of the tissue, including artefacts such as folds and tears. In this paper, 
we present a probabilistic model of spatial deformation that yields reconstructions for multiple histological stains that that 
are jointly smooth, robust to outliers, and follow the reference shape. The model relies on a spanning tree of latent transforms 
connecting all the sections and slices of the reference volume, and assumes that the registration between any pair of images can be seen
as a noisy version of the composition of (possibly inverted) latent transforms connecting the two images. Bayesian inference is used to 
compute the most likely latent transforms given a set of pairwise registrations between image pairs within and across modalities. 
We consider two likelihood models: Gaussian (L2-norm, which can be minimised in closed form) and Laplacian (L1-norm, minimised with linear programming). 
Results on synthetic deformations on multiple MR modalities, show that our method can accurately and robustly register multiple contrasts even 
in the presence of outliers. The framework is used for accurate 3D reconstruction of two stains (Nissl and parvalbumin) from the Allen human brain atlas, 
showing its benefits on real data with severe distortions. Moreover, we also provide the registration of the reconstructed volume to MNI space, 
bridging the gaps between two of the most widely used atlases in histology and MRI. The 3D reconstructed volumes and atlas registration can be 
downloaded from https://openneuro.org/datasets/ds003590. The code is freely available at https://github.com/acasamitjana/3dhirest.
