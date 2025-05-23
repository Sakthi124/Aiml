import pandas as pd

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

# Step 1: Load the Excel dataset (replace with your file path)

df = pd.read_excel('student_marks.xlsx',header=1)

# Step 2: Preview the data to ensure it's loaded correctly

print("Dataset:")

print(df)

# Step 3: Extract relevant columns (Maths and Science marks) for clustering

X = df[['Maths', 'Science']]

# Step 4: Apply K-Means clustering (using 2 clusters for simplicity)
kmeans = KMeans(n_clusters=2, random_state=0)

kmeans_labels = kmeans.fit_predict(X)

# Step 5: Add KMeans cluster labels to the DataFrame

df['Cluster'] = kmeans_labels

# Step 6: Plot the clusters

plt.figure(figsize=(8, 6))

plt.scatter(df[df['Cluster'] == 0]['Maths'], df[df['Cluster'] == 0]['Science'],s=100, c='blue', 

label='Cluster 0')

plt.scatter(df[df['Cluster'] == 1]['Maths'], df[df['Cluster'] == 1]['Science'],s=100, c='red', 

label='Cluster 1')

# Mark the centroids

centroids = kmeans.cluster_centers_

plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='red', marker='X', label='Centroids')

# Labels and title

plt.xlabel('Maths Marks')

plt.ylabel('Science Marks')

plt.title('Student Clusters Based on Marks')

plt.legend()

plt.grid(True)

plt.show()

# Step 7: Display the DataFrame with cluster labels

print("\nCluster Results for Each Student:")

print(df)
