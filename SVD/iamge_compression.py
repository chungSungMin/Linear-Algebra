import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


image = Image.open('/Users/jeongseungmin/Desktop/Study/transformer/Linear-Algebra/SVD/shark.jpeg')
A = np.array(image, dtype=float)

A_R = A[:, :, 0]
A_G = A[:, :, 1]
A_B = A[:, :, 2]

U_R, S_R, Vt_R = np.linalg.svd(A_R, full_matrices=False)
U_G, S_G, Vt_G = np.linalg.svd(A_G, full_matrices=False)
U_B, S_B, Vt_B = np.linalg.svd(A_B, full_matrices=False)


non_zero_R = np.sum(S_R > 0)
non_zero_G = np.sum(S_G > 0)
non_zero_B = np.sum(S_B > 0)
print(f"R 채널의 비영 고유값 개수: {non_zero_R}")
print(f"G 채널의 비영 고유값 개수: {non_zero_G}")
print(f"B 채널의 비영 고유값 개수: {non_zero_B}")


k = 30
A_R_compressed = np.dot(U_R[:, :k], np.dot(np.diag(S_R[:k]), Vt_R[:k, :]))
A_G_compressed = np.dot(U_G[:, :k], np.dot(np.diag(S_G[:k]), Vt_G[:k, :]))
A_B_compressed = np.dot(U_B[:, :k], np.dot(np.diag(S_B[:k]), Vt_B[:k, :]))


A_compressed = np.stack([A_R_compressed, A_G_compressed, A_B_compressed], axis=2)
A_compressed = np.clip(A_compressed, 0, 255).astype('uint8')

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Origin image : 188 vectors')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('compressed image : 30 vectors')
plt.imshow(A_compressed)
plt.axis('off')

plt.show()

