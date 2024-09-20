import numpy as np
from gtda.diagrams import Amplitude
from gtda.homology import VietorisRipsPersistence

persistence = VietorisRipsPersistence(metric = 'euclidean',homology_dimensions=[0,1,2],n_jobs=-1,collapse_edges=True)

""""
model is the autoencoder defined by the user
dataloader is the dataset
number of epoch
criterion
optimiser
device
"""
def taelcore(model, dataloader, num_epochs, criterion,optimizer,device=False):
    losses=[]
    for epoch in range(num_epochs):
        epoch_loss = 0.0
        model.train()  # Set model to training mode
        for data, target in dataloader:
            if device:
                data = data.to(device)
                target = target.to(device)

            # Forward pass
            output = model(data)

            e=model.encoder(data).detach().numpy()

            dy=persistence.fit_transform(output.detach().numpy()[None,:,:])
            dz=persistence.fit_transform(e[None,:,:])
            dx=persistence.fit_transform(data[None,:,:])
            
            a1=Amplitude(metric='bottleneck').fit_transform(dx)
            a2=Amplitude(metric='wasserstein').fit_transform(dx)
            a3=Amplitude(metric='landscape').fit_transform(dx)
            a4=Amplitude(metric='betti').fit_transform(dx)
            a5=Amplitude(metric='persistence_image').fit_transform(dx)
            
            a=a1+a2+a3+a4+a5
            
            b1=Amplitude(metric='bottleneck').fit_transform(dz)
            b2=Amplitude(metric='wasserstein').fit_transform(dz)
            b3=Amplitude(metric='landscape').fit_transform(dz)
            b4=Amplitude(metric='betti').fit_transform(dz)
            b5=Amplitude(metric='persistence_image').fit_transform(dz)
            
            b=b1+b2+b3+b4+b5
            
            c1=Amplitude(metric='bottleneck').fit_transform(dy)
            c2=Amplitude(metric='wasserstein').fit_transform(dy)
            c3=Amplitude(metric='landscape').fit_transform(dy)
            c4=Amplitude(metric='betti').fit_transform(dy)
            c5=Amplitude(metric='persistence_image').fit_transform(dy)
            
            c=c1+c2+c3+c4+c5
        
            
            l1=(np.linalg.norm(a-b)**2)/2
        
            l2=(np.linalg.norm(b-c)**2)/2
        
            l=l1+l2


            loss = criterion(output, target)+(1e-5)*l

            # Backward pass and optimization
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # Accumulate loss for this epoch
            # epoch_loss += loss.item() * data.size(0)
            epoch_loss += loss.data

        
        # Calculate average loss over the epoch
        epoch_loss /= len(dataloader.dataset)
        losses.append(epoch_loss)
        print(f'Epoch {epoch + 1}/{num_epochs}, Loss: {epoch_loss}')

    return model, losses
