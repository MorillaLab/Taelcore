# TaelCore

[![License](https://img.shields.io/badge/License-GPLv3-green)](https://choosealicense.com/licenses/gpl-3.0/)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/MorillaLab/TopoTransformers/)
[![Doi](https://img.shields.io/badge/Doi-10.1016-blue)](https://doi.org/10.1016/j.compbiomed.2024.107969)
[![Pywheels](https://img.shields.io/pypi/dm/taelcore)](https://www.piwheels.org/project/taelcore/)

Novel Dimensionality Reduction Technique

[Gouiaa et al.  **Novel dimensionality reduction method, Taelcore, enhances lung transplantation risk prediction**. 2024. *Computers in Biology and Medicine*.](
https://www.sciencedirect.com/science/article/pii/S0010482524000532) 👁️

We present a new approach to predict the risk of acute cellular rejection (ACR)
after lung transplantation by using machine learning algorithms, such as Multilayer Perceptron
(MLP) or Autoencoder (AE), and combining them with topological data analysis (TDA)
tools. Our proposed method, named topological autoencoder with best linear combination
for optimal reduction of embeddings (Taelcore), effectively reduces the dimensionality of
high-dimensional datasets and yields better results compared to other models. We validate
the effectiveness of Taelcore in reducing the prediction error rate on three datasets. Furthermore,
we demonstrate that Taelcore’s topological improvements have a positive effect on
the majority of the machine learning algorithms used. By providing a new way to diagnose
patients and detect complications early, this work contributes to improved clinical outcomes
in lung transplantation.

![Taelcore workflow](https://github.com/MorillaLab/Taelcore/blob/main/Figure_3_3.png)


A comprehensive comparison of the latent space representations obtained by our proposed method and several baseline techniques, namely Autoencoder, PCA, t-SNE, and UMAP, across different datasets. (a) Shapes Dataset: The latent space representations of the Shapes dataset are depicted for our method, Autoencoder, PCA, t-SNE, and UMAP. Our method not only effectively preserves the intrinsic structure but also out- performs the other techniques in terms of separation. This is evident from the distinct and well-separated clusters observed in our method’s representation. (b) Iris Dataset: The latent space representations of the Iris dataset are presented for our method, Autoencoder, PCA, t-SNE, and UMAP. Our method demonstrates a notably more linear separation between the classes compared to the other methods. This indicates its efficacy in capturing the essential discriminative information present in the dataset. (c) Lung Transplantation Dataset: The latent space representations of the lung transplantation dataset are illustrated for our method, Autoencoder, PCA, t-SNE, and UMAP. Our method exhibits a significant linear separation between the ACR and non-ACR groups of patients while maintaining a lower degree of sparsity compared to the alternative techniques.

![Taelcore representation learning](https://github.com/MorillaLab/Taelcore/blob/main/Figure_4_4.png)

# Python 
#### Installation with `pip`

The Python version of TaelCore can be installed by running the following from a terminal:
```ruby
# bash to install the package in a virtualenv
pip3 install taelcore
```
