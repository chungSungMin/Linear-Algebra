import numpy as np
import matplotlib.pyplot as plt


def visualization(x, y, z, compressed_data): 
    """ pca결과를 시각화 합니다.

    Args:
        x (ndarray): dim 1을 의미
        y (ndarray): dim 2을 의미
        z (ndarray): dim 3을 의미
        compressed_data (ndarray): pca연산을 통해서 압축된 데이터를 의미 ( 3D -> 2D )
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='blue', alpha=0.7)
    plt.title('Original image in 3D')
    plt.show()

    compressed_x = compressed_data[:, 0]
    compressed_y = compressed_data[:, 1]

    plt.figure()
    plt.scatter(compressed_x, compressed_y, c='red', alpha=0.7)
    plt.title('Compressed into 2D')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.grid()
    plt.show()


def pca_operation(random_data, data_mean):
    """PCA연산을 진행합니다

    Args:
        random_data (ndarray): 임의로 만들어진 (100, 3) 크기의 행렬
        data_mean (ndarray): 각 차원의 평균이 담긴 행렬
    """

    normalized_data = random_data - data_mean

    covariance_matrix = np.cov(normalized_data.T)

    eigen_value, eigen_vector = np.linalg.eig(covariance_matrix)

    print(f'eigen value : {eigen_value}')
    print(f'eigen vector : {eigen_vector}')

    sorted_indices = np.argsort(eigen_value)[::-1]
    sorted_eigen_value = eigen_value[sorted_indices]
    sorted_eigen_vector = eigen_vector[:, sorted_indices]

    k = 2
    pca_vectors = sorted_eigen_vector[:, :k]
    compressed_data = np.dot(normalized_data, pca_vectors)

    x = normalized_data[:, 0]
    y = normalized_data[:, 1]
    z = normalized_data[:, 2]

    visualization(x, y, z, compressed_data)


if __name__ == '__main__' : 
    random_data = np.random.rand(100, 3)
    data_mean = np.mean(random_data, axis=0)
    pca_operation(random_data, data_mean)