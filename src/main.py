#%%
from scipy.spatial import ConvexHull
import pandas as pd
import matplotlib.pyplot as plt
import MyConvexHull as mch
from sklearn import datasets

while (True):
    x = input("Pilih Dataset yang diinginkan (iris, wine, breast_cancer) :")
    if x == "iris":
        data = datasets.load_iris()
        #create a DataFrame
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['Target'] = pd.DataFrame(data.target)
        print("ATTRIBUTES\n 1. Sepal Length\n 2. Sepal Width\n 3. Petal Length\n 4. Petal Width")
        Attributes= ["Sepal Length","Sepal Width","Petal Length","Petal Width"]
        df.head()
        idx_x = int(input("Attribute pertama : "))
        idx_y = int(input("Attribute kedua : "))        
        plt.figure(figsize = (10, 6))
        colors = ['b','r','g','p']
        title = Attributes[idx_x-1] + " vs " + Attributes[idx_y-1]
        plt.title(title)
        plt.xlabel(data.feature_names[idx_x-1])
        plt.ylabel(data.feature_names[idx_y-1])
        for i in range(len(data.target_names)):
            bucket = df[df['Target'] == i]
            bucket = bucket.iloc[:,[idx_x-1,idx_y-1]].values
            hull = mch.ConvexHull(bucket)
            # print("HASIL Koordinat : ",hull)
            x, y = zip(*hull)
            plt.plot(x,y,c=colors[i])
            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
            plt.legend()
        
        plt.figure(figsize = (10, 6))
        colors = ['b','r','g','p']
        title = Attributes[idx_x-1] + " vs " + Attributes[idx_y-1] + " (Library Scipy)"
        plt.title(title)
        plt.xlabel(data.feature_names[idx_x-1])
        plt.ylabel(data.feature_names[idx_y-1])
        for j in range(len(data.target_names)):
            bucket = df[df['Target'] == j]
            bucket = bucket.iloc[:,[idx_x-1,idx_y-1]].values
            hull = ConvexHull(bucket) 
            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[j])
            for simplex in hull.simplices:
                plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[j])
            plt.legend()
        break
    elif x == "wine":
        data = datasets.load_wine()
        #create a DataFrame
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['Target'] = pd.DataFrame(data.target)
        print("ATTRIBUTES\n 1. Alcohol\n 2. Malic Acid\n 3. Ash\n 4. Alcalinity of ash\n 5. Magnesium\n 6. Total phenols\n 7. Vlavanoids")
        Attributes= ["Alcohol","Malic Acid","Ash","Alcalinity of ash","Magnesium","Total phenols","Flavanoids"]
        df.head()
        idx_x = int(input("Attribute pertama : "))
        idx_y = int(input("Attribute kedua : "))        
        plt.figure(figsize = (10, 6))
        colors = ['b','r','g','p']
        title = Attributes[idx_x-1] + " vs " + Attributes[idx_y-1]
        plt.title(title)
        plt.xlabel(data.feature_names[idx_x-1])
        plt.ylabel(data.feature_names[idx_y-1])
        for i in range(len(data.target_names)):
            bucket = df[df['Target'] == i]
            bucket = bucket.iloc[:,[idx_x-1,idx_y-1]].values
            hull = mch.ConvexHull(bucket)
            # print("HASIL Koordinat : ",hull)
            x, y = zip(*hull)
            plt.plot(x,y,c=colors[i])
            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
            plt.legend()
            
        plt.figure(figsize = (10, 6))
        colors = ['b','r','g','p']
        title = Attributes[idx_x-1] + " vs " + Attributes[idx_y-1] + " (Library Scipy)"
        plt.title(title)
        plt.xlabel(data.feature_names[idx_x-1])
        plt.ylabel(data.feature_names[idx_y-1])
        for j in range(len(data.target_names)):
            bucket = df[df['Target'] == j]
            bucket = bucket.iloc[:,[idx_x-1,idx_y-1]].values
            hull = ConvexHull(bucket) 
            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[j])
            for simplex in hull.simplices:
                plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[j])
            plt.legend()
        break
    elif x == "breast_cancer":
        data = datasets.load_breast_cancer()
        #create a DataFrame
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['Target'] = pd.DataFrame(data.target)
        print("ATTRIBUTES\n 1. Radius\n 2. Texture\n 3. Perimeter\n 4. Area\n 5. Smoothness\n 6. Compactness\n 7. Concavity")
        Attributes= ["Radius","Texture","Perimeter","Area","Smoothness","Compactness","Concavity"]
        df.head()
        idx_x = int(input("Attribute pertama : "))
        idx_y = int(input("Attribute kedua : "))        
        plt.figure(figsize = (10, 6))
        colors = ['b','r','g']
        title = Attributes[idx_x-1] + " vs " + Attributes[idx_y-1]
        plt.title(title)
        plt.xlabel(data.feature_names[idx_x-1])
        plt.ylabel(data.feature_names[idx_y-1])
        for i in range(len(data.target_names)):
            bucket = df[df['Target'] == i]
            bucket = bucket.iloc[:,[idx_x-1,idx_y-1]].values
            hull = mch.ConvexHull(bucket)
            # print("HASIL Koordinat : ",hull)
            x, y = zip(*hull)
            plt.plot(x,y,c=colors[i])
            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
            plt.legend()
        plt.figure(figsize = (10, 6))
        colors = ['b','r','g','p']
        title = Attributes[idx_x-1] + " vs " + Attributes[idx_y-1] + " (Library Scipy)"
        plt.title(title)
        plt.xlabel(data.feature_names[idx_x-1])
        plt.ylabel(data.feature_names[idx_y-1])
        for j in range(len(data.target_names)):
            bucket = df[df['Target'] == j]
            bucket = bucket.iloc[:,[idx_x-1,idx_y-1]].values
            hull = ConvexHull(bucket) 
            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[j])
            for simplex in hull.simplices:
                plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[j])
            plt.legend()
        break
    else:
        print("Gunakan dataset sesuai pilihan!")
# %%