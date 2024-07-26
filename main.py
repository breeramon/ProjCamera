import cv2

def camPossiveis(max_cameras=10):
  camerasPossiveis = []
  for index in range(max_cameras):
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
      camerasPossiveis.append(index)
      cap.release()
  return camerasPossiveis

cameras = camPossiveis()
print(f"Cameras possíveis: {cameras}")

if cameras:
  cap = cv2.VideoCapture(cameras[0])
  if not cap.isOpened():
    print("Erro: Não foi possível abrir a câmera")
  else:
    while True:
      ret, frame = cap.read()
      if ret:
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
      else:
        print("Erro: Não foi possível capturar o frame.")
        break
    cap.release()
    cv2.destroyAllWindows()
else:
  print("Nenhuma câmera encontrada.")
