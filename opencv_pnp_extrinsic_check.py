import cv2
import numpy as np

img = cv2.imread("./pair/jpeg/1.jpeg")

size = img.shape

image_points_2d = np.array([
    (1737,490),(1725,720),(1668,601),(1803,614),
], dtype="double")

figure_points_3d = np.array([
(2.891095,-2.881021,0.213903),
(2.911755,-2.853393,-0.595715),
(3.191884,-2.718428,-0.169028),
(2.562569,-2.998263,-0.237363),
])

distortion_coeffs = np.array([-0.309502719001483, 0.0678123735430055, 0, 0, 0.000000])
matrix_camera = np.array(
                         [[1032.12381297729, 0.000000, 1023.06962902607],
                 [0.000000, 1042.83746348152, 551.011633212484],
                 [0.000000, 0.000000, 1.000000]], dtype = "double")

success, vector_rotation, vector_translation = cv2.solvePnP(figure_points_3d, image_points_2d, matrix_camera, distortion_coeffs, flags=cv2.SOLVEPNP_EPNP)
# nose_end_point2D, jacobian = cv2.projectPoints(np.array([(0.0, 0.0, 1000.0)]), vector_rotation, vector_translation, matrix_camera, distortion_coeffs)
print("vector_translation",vector_translation)
mapping_point2d, jacobian = cv2.projectPoints(figure_points_3d, vector_rotation, vector_translation, matrix_camera, distortion_coeffs)
# print(nose_end_point2D)
# print(jacobian)
for p in mapping_point2d:
    # print("p", p)
    # print("p shape", p.shape)

    cv2.circle(img, (int(p[0][0]), int(p[0][1])), 3, (0,0,255), -1)
# point1 = ( int(image_points_2d[0][0]), int(image_points_2d[0][1]))
for p in mapping_point2d:
    # print("p", p)
    # print("p shape", p.shape)

    cv2.circle(img, (int(p[0][0]), int(p[0][1])), 1, (0,255,0), -1)
# point2 = ( int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))
# cv2.line(img, point1, point2, (255,255,255), 2)
cv2.imshow("Final",img)
cv2.waitKey(0)
cv2.destroyAllWindows()