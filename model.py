import torch
import torch.nn as nn
import numpy as np


class MyModel(torch.nn.Module):
    """
    MyModel is a custom neural network model for image classification and segmentation and vectorization.
    """

    def __init__(self, output_size=30):
        """Initialize the model.

        Args:
            input_size (int): Size of the input features.
            hidden_size (int): Size of the hidden layers.
            output_size (int): Size of the output layer (number of classes).
        """
        super(MyModel, self).__init__()
        self.backbone =  # ‼️‼️‼️‼️ Define your backbone ‼️‼️‼️‼️

        self.species_classifier =  # ‼️‼️‼️‼️ Define you classifier ‼️‼️‼️‼️

        self.segmentation_head =  # ‼️‼️‼️‼️ Define your segmentation head ‼️‼️‼️‼️

    def forward(self, x):
        """Forward pass for the model.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            tuple: (species, masks, embeddings)
            species (torch.Tensor): The species classification logits.
            masks (torch.Tensor): The segmentation masks.
            embeddings (torch.Tensor): The feature embeddings.
        """
        # ‼️‼️‼️‼️ Define the forward pass ‼️‼️‼️‼️
        return species, masks, embeddings

    def get_embedding(self, x):
        """Get the feature embeddings from the model.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: The feature embeddings.
        """
        # ‼️‼️‼️‼️ Implement the embedding extraction ‼️‼️‼️‼️
        return embeddings
